import io

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse
from .forms import JobForm, CLForm, CLForm_Text, CLForm_Main, SourceForm
from django.http import HttpResponseRedirect, JsonResponse
from .models import Job, CoverLetter, Source, UserConsent
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
        essential = request.POST.get('essential_cookies', False)
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
    paginator_head = Paginator(Job.objects.filter(user=current_user).order_by('-id'), 5)
    page = request.GET.get('page')
    job_all = paginator_head.get_page(page)

    sources_base = [
        "https://www.indeed.de",
        "https://www.stepstone.de",
        "https://www.monster.de",
        "https://www.xing.com/jobs",
        "https://www.linkedin.com",
        "https://www.glassdoor.de",
        "https://www.jobware.de",
        "https://www.kimeta.de",
        "https://www.stellenanzeigen.de"
    ]

    sources_user = Source.objects.filter(user=current_user).order_by('-id')

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
    edit_mode_text = request.GET.get('edit_mode_text', '0') == '1'
    edit_mode_update = request.GET.get('edit_mode_update', '0') == '1'
    
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

    return render(request, 'JAB_Main/cl_main.html', {
        'job_case':job_case,
        'cl_case': cl_case,
        'form_text': form_text,
        'edit_mode_text': edit_mode_text,
        'form_update':form_update,
        'edit_mode_update':edit_mode_update
    })

@login_required
def cl_proofread(request, cl_id):
    current_user = request.user
    cl_case = CoverLetter.objects.get(pk=cl_id, user=current_user)
    job_case = cl_case.job
    edit_mode_proofread_main = request.GET.get('edit_mode_proofread_main', '0') == '1'

    if request.method == "POST" and edit_mode_proofread_main:
        form_main = CLForm_Main(request.POST, instance=cl_case)
        if form_main.is_valid() and request.GET.get('edit_mode_proofread_main', '0') == '1':
            form_main.save()
            return HttpResponseRedirect(reverse('cl_proofread', args=[cl_id]))
    else:
        form_main = CLForm_Main(instance=cl_case)
    
    return render(request, 'JAB_Main/cl_proofread.html', {
        'cl_case':cl_case,
        'job_case':job_case,
        'form_main':form_main,
        'edit_mode_proofread_main':edit_mode_proofread_main
    })

@login_required
def cl_download(request, cl_id):
    current_user = request.user
    cl_case = CoverLetter.objects.get(pk=cl_id, user=current_user) 
    job_case = cl_case.job
    buf = io.BytesIO()
    canvas_case = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # pdfmetrics.registerFont(TTFont('Verdana', 'JobApplicationBestie/JAB_Main/templates/JAB_Main/Verdana.ttf'))
    canvas_case.setFont('Helvetica', 12)
    y_position = inch
    
    canvas_case.drawRightString(7*inch, y_position, cl_case.main_self_name)
    y_position += 20
    
    canvas_case.drawRightString(7*inch, y_position, cl_case.main_self_address)
    y_position += 40

    canvas_case.drawString(inch, y_position, job_case.company)
    y_position += 20
    
    canvas_case.drawString(inch, y_position, job_case.address)
    y_position += 40
    
    canvas_case.drawString(inch, y_position, cl_case.main_subject)
    y_position += 20
    
    canvas_case.drawString(inch, y_position, cl_case.text)
    
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