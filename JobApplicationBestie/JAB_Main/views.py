import io
import json

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse
from .forms import JobForm, CLForm, CLForm_Text, CLForm_Main, SourceForm, JobForm_ReferenceNotes, JobCaseSelectionForm, JobForm_Company, ReferenceProjectForm
from django.http import HttpResponseRedirect, JsonResponse
from .models import Job, CoverLetter, Source, UserConsent, ReferenceProject
from django.core.paginator import Paginator


from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont





def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('jobs'))
    else:
        return render(request, 'JAB_Main/index.html', {})

def privacy_policy(request):
    return render(request, 'JAB_Main/privacy_policy.html', {})
        
def terms_conditions(request):
    return render(request, 'JAB_Main/terms_conditions.html', {})

def data_security(request):
    return render(request, 'JAB_Main/data_security.html', {})

def accept_cookies(request):
    if request.method == 'POST':
        user_ip = request.META.get('REMOTE_ADDR')
        essential = json.loads(request.POST.get('essential_cookies', False))
        consent = UserConsent(
            user_ip=user_ip,
            essential_cookies=essential
        )
        consent.save()
        return JsonResponse({'message': 'Consent recorded successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)

@login_required
def job_add(request):
    submitted = False
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            current_user = request.user
            form_case = form.save(commit=False)
            form_case.user = current_user
            form_case.save()
            job = Job.objects.get(pk=form_case.id)
            cover_letter = CoverLetter(job=job, user=current_user)
            cover_letter.save()
            return HttpResponseRedirect(reverse('jobs')) 

    else:   
        form = JobForm
        if 'submitted' in request.GET:
            submitted = True 
    return render(request, 'JAB_Main/job_add.html', {'form':form, 'submitted':submitted})

@login_required
def jobs(request):
    current_user = request.user
    paginator_head = Paginator(Job.objects.filter(user=current_user).order_by('-id'), 8)
    page = request.GET.get('page')
    job_all = paginator_head.get_page(page)

    sources_base = [
        "https://www.indeed.de",
        "https://www.stepstone.de",
        "https://www.xing.com/jobs",
        "https://www.linkedin.com/jobs/search/?keywords=data%20analyst"
    ]

    sources_user = Source.objects.filter(user=current_user).order_by('id')

    return render(request, 'JAB_Main/jobs.html', {
        'job_all':job_all,
        'sources_base':sources_base,
        'sources_user':sources_user
    })
    
@login_required
def job_update(request, job_id):
    current_user = request.user
    job_case = Job.objects.get(pk=job_id, user=current_user)
    form = JobForm(request.POST or None, instance=job_case)
    if form.is_valid():
        form.save()
        return redirect('jobs')

    return render(request, 'JAB_Main/job_update.html', {
        'job_case':job_case,
        'form':form
    })

@login_required
def job_delete(request, job_id):
    current_user = request.user
    job_case = Job.objects.get(pk=job_id, user=current_user) 
    job_case.delete()
    return redirect('jobs')

@login_required
def cl_main(request, job_id):
    current_user = request.user
    job_case = Job.objects.get(pk=job_id, user=current_user)
    cl_case = job_case.cover_letters_job
    reference_project_cases = ReferenceProject.objects.filter(user=current_user).order_by('-id')
    edit_mode_text = request.GET.get('edit_mode_text', '0') == '1'
    edit_mode_update = request.GET.get('edit_mode_update', '0') == '1'
    edit_mode_reference_notes = request.GET.get('edit_mode_reference_notes', '0') == '1'
    
    if request.method == "POST" and edit_mode_text:
        form_text = CLForm_Text(request.POST, instance=cl_case)
        if form_text.is_valid() and request.GET.get('edit_mode_text', '0') == '1':
            form_text.save()
            job_id = cl_case.job.id
            return HttpResponseRedirect(reverse('cl_main', args=[job_id]))
    else:
        form_text = CLForm_Text(instance=cl_case)

    if request.method == "POST" and edit_mode_update:
        form_update = CLForm(request.POST, instance=cl_case)
        if form_update.is_valid() and request.GET.get('edit_mode_update', '0') == '1':
            form_update.save()
            job_id = cl_case.job.id
            return HttpResponseRedirect(reverse('cl_main', args=[job_id]))
    else:
        form_update = CLForm(instance=cl_case)

    if request.method == "POST" and edit_mode_reference_notes:
        form_reference_notes = JobForm_ReferenceNotes(request.POST, instance=job_case)
        if form_reference_notes.is_valid() and request.GET.get('edit_mode_reference_notes', '0') == '1':
            form_reference_notes.save()
            job_id = cl_case.job.id
            return HttpResponseRedirect(reverse('cl_main', args=[job_id]))
    else:
        form_reference_notes = JobForm_ReferenceNotes(instance=job_case)

    selected_job_case = None
    if request.method == 'POST':
        form_job_case = JobCaseSelectionForm(current_user, request.POST)
        if form_job_case.is_valid():
            case = form_job_case.cleaned_data['case_select']
            if case:
                selected_job_case = Job.objects.get(pk=case.id)
            else:
                selected_job_case = None
    else:
        form_job_case = JobCaseSelectionForm(current_user)

    return render(request, 'JAB_Main/cl_main.html', {
        'job_case':job_case,
        'cl_case': cl_case,
        'form_text': form_text,
        'edit_mode_text': edit_mode_text,
        'form_update':form_update,
        'edit_mode_update':edit_mode_update,
        'form_reference_notes':form_reference_notes,
        'edit_mode_reference_notes':edit_mode_reference_notes,
        'form_job_case':form_job_case,
        'selected_job_case': selected_job_case,
        'reference_project_cases': reference_project_cases
    })

@login_required
def cl_proofread(request, cl_id):
    current_user = request.user
    cl_case = CoverLetter.objects.get(pk=cl_id, user=current_user)
    job_case = cl_case.job
    edit_mode_proofread_main = request.GET.get('edit_mode_proofread_main', '0') == '1'
    edit_mode_proofread_company = request.GET.get('edit_mode_proofread_company', '0') == '1'

    if request.method == "POST" and edit_mode_proofread_main:
        form_main = CLForm_Main(request.POST, instance=cl_case)
        if form_main.is_valid() and request.GET.get('edit_mode_proofread_main', '0') == '1':
            form_main.save()
            return HttpResponseRedirect(reverse('cl_proofread', args=[cl_id]))
    else:
        form_main = CLForm_Main(instance=cl_case)

    if request.method == "POST" and edit_mode_proofread_company:
        form_proofread_company = JobForm_Company(request.POST, instance=job_case)
        if form_proofread_company.is_valid() and request.GET.get('edit_mode_proofread_company', '0') == '1':
            form_proofread_company.save()
            return HttpResponseRedirect(reverse('cl_proofread', args=[cl_id]))
    else:
        form_proofread_company = JobForm_Company(instance=job_case)
    
    return render(request, 'JAB_Main/cl_proofread.html', {
        'cl_case':cl_case,
        'job_case':job_case,
        'form_main':form_main,
        'edit_mode_proofread_main':edit_mode_proofread_main,
        'form_proofread_company':form_proofread_company,
        'edit_mode_proofread_company':edit_mode_proofread_company
    })

@login_required
def cl_download(request, cl_id):
    
    def split_long_string(data, max_width):
        words = data.split()
        lines = []
        current_line = []

        for word in words:
            if len(' '.join(current_line + [word])) > max_width:
                lines.append(' '.join(current_line))
                current_line = [word]
            else:
                current_line.append(word)

        lines.append(' '.join(current_line))

        return lines

    current_user = request.user
    cl_case = CoverLetter.objects.get(pk=cl_id, user=current_user) 
    job_case = cl_case.job
    pdfmetrics.registerFont(TTFont('TNR', 'JobApplicationBestie/JAB_Main/fonts/times.ttf'))
    pdfmetrics.registerFont(TTFont('TNRB', 'JobApplicationBestie/JAB_Main/fonts/timesbd.ttf'))


    buf = io.BytesIO()
    y_position = inch
    x_right = 7.5*inch
    x_left = 1*inch
    max_width = 100

    canvas_case = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    
    canvas_case.setFillColorRGB(0, 0, 0)
    canvas_case.rect(0, 0, 0.5 * inch, letter[1], fill=1)

    canvas_case.setFont('TNRB', 10)
    data_put = cl_case.main_self_name if cl_case.main_self_name is not None else ''
    canvas_case.drawRightString(x_right, y_position, data_put)
    y_position += 20
    
    canvas_case.setFont('TNR', 10)
    data_put = cl_case.main_self_address if cl_case.main_self_address is not None else ''
    lines = data_put.split('\n')
    total_lines = len(lines)
    for i, line in enumerate(lines):
        if i != total_lines -1:
            canvas_case.drawRightString(x_right, y_position, line[:-1])
        else:  
            canvas_case.drawRightString(x_right, y_position, line)
        y_position += 12
    y_position += 40

    canvas_case.setFont('TNRB', 10)
    data_put = job_case.company if job_case.company is not None else ''
    canvas_case.drawString(x_left, y_position, data_put)
    y_position += 20
    
    canvas_case.setFont('TNR', 10)
    data_put = job_case.address if job_case.address is not None else ''
    lines = data_put.split('\n')
    total_lines = len(lines)
    for i, line in enumerate(lines):
        if i != total_lines -1:
            canvas_case.drawString(x_left, y_position, line[:-1])
        else:  
            canvas_case.drawString(x_left, y_position, line)
        y_position += 12
    y_position += 20
    
    canvas_case.setFont('TNR', 10)
    data_put = cl_case.main_cover_letter_date if cl_case.main_cover_letter_date is not None else ''
    canvas_case.drawRightString(x_right, y_position, str(data_put.strftime("%d.%m.%Y")))
    y_position += 40

    canvas_case.setFont('TNRB', 10)
    data_put = cl_case.main_subject if cl_case.main_subject is not None else ''
    canvas_case.drawString(x_left, y_position, 'Subject: '+data_put)
    y_position += 20
    
    canvas_case.setFont('TNR', 10)
    data_put = cl_case.text if cl_case.text is not None else ''
    lines = data_put.split('\n')
    total_lines = len(lines)
    
    for i, line in enumerate(lines):
        text_lines = split_long_string(line, max_width)
        total_lines_inside = len(text_lines)
        for j, line_put in enumerate(text_lines):
            if (i != total_lines -1) & (j == total_lines_inside -1):
                canvas_case.drawString(x_left, y_position, line_put[:-1])
            else:  
                canvas_case.drawString(x_left, y_position, line_put)
            y_position += 12

    canvas_case.showPage()
    canvas_case.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='CoverLetter.pdf')

@login_required
def ui_dev_index_footer(request):
    current_user = request.user
    if current_user.is_superuser:
        return render(request, 'JAB_Main/index/index_footer.html', {})


@login_required
def source_add(request):
    submitted = False
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            current_user = request.user
            form_case = form.save(commit=False)
            form_case.user = current_user
            form_case.save()
            return HttpResponseRedirect(reverse('jobs')) 

    else:   
        form = SourceForm
        if 'submitted' in request.GET:
            submitted = True 
    return render(request, 'JAB_Main/source_add.html', {'form':form, 'submitted':submitted})

@login_required
def source_update(request, source_id):
    current_user = request.user
    source_case = Source.objects.get(pk=source_id, user=current_user)
    form = SourceForm(request.POST or None, instance=source_case)
    if form.is_valid():
        form.save()
        return redirect('jobs')

    return render(request, 'JAB_Main/source_update.html', {
        'source_case':source_case,
        'form':form
    })

@login_required
def source_delete(request, source_id):
    current_user = request.user
    source_case = Source.objects.get(pk=source_id, user=current_user) 
    source_case.delete()
    return redirect('jobs')

@login_required
def references_main(request):
    current_user = request.user
    reference_project_cases = ReferenceProject.objects.filter(user=current_user).order_by('-id')
    
    return render(request, 'JAB_Main/references_main.html', {
        'reference_project_cases':reference_project_cases, 
    })

@login_required
def project_add(request):
    submitted = False
    if request.method == 'POST':
        form = ReferenceProjectForm(request.POST)
        if form.is_valid():
            current_user = request.user
            form_case = form.save(commit=False)
            form_case.user = current_user
            form_case.save()
            return HttpResponseRedirect(reverse('references_main')) 
    else:   
        form = ReferenceProjectForm
        if 'submitted' in request.GET:
            submitted = True 
    return render(request, 'JAB_Main/project_add.html', {'form':form, 'submitted':submitted})

@login_required
def project_update(request, project_id):
    current_user = request.user
    project_case = ReferenceProject.objects.get(pk=project_id, user=current_user)
    form = ReferenceProjectForm(request.POST or None, instance=project_case)
    if form.is_valid():
        form.save()
        return redirect('references_main')

    return render(request, 'JAB_Main/project_update.html', {
        'project_case':project_case,
        'form':form
    })

@login_required
def project_delete(request, project_id):
    current_user = request.user
    project_case = ReferenceProject.objects.get(pk=project_id, user=current_user) 
    project_case.delete()
    return redirect('references_main')

@login_required
def project_main(request, project_id):
    current_user = request.user
    project_case = ReferenceProject.objects.get(pk=project_id, user=current_user)
    edit_mode_project = request.GET.get('edit_mode_project', '0') == '1'
    if request.method == "POST" and edit_mode_project:
        form_project = ReferenceProjectForm(request.POST, instance=project_case)
        if form_project.is_valid() and request.GET.get('edit_mode_project', '0') == '1':
            form_project.save()
            return HttpResponseRedirect(reverse('project_main', args=[project_id]))
    else:
        form_project = ReferenceProjectForm(instance=project_case)

    return render(request, 'JAB_Main/project_main.html', {
        'project_case':project_case,
        'form_project': form_project,
        'edit_mode_project': edit_mode_project,
    })
