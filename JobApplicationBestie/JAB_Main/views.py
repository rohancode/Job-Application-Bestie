import io

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse
from .forms import JobForm, CLForm
from django.http import HttpResponseRedirect
from .models import Job, CoverLetter
from django.core.paginator import Paginator

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('jobs'))
    else:
        return render(request, 'JAB_Main/index.html', {})

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
            job_id = form_case.id
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
    return render(request, 'JAB_Main/jobs.html', {
        'job_all':job_all
    })

@login_required
def job_main(request, job_id):
    current_user = request.user
    job_case = Job.objects.get(pk=job_id, user=current_user)
    cl_cases = job_case.cover_letters_job.all().order_by('-id')
    return render(request, 'JAB_Main/job_main.html', {
        'job_case':job_case,
        'cl_cases': cl_cases
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
def cl_add(request, job_id):
    submitted = False
    if request.method == 'POST':
        form = CLForm(request.POST)
        if form.is_valid():
            current_user = request.user
            form_case = form.save(commit=False)
            form_case.user = current_user
            job_case = Job.objects.get(pk=job_id, user=current_user) 
            form_case.job = job_case
            form_case.save()
            job_id = job_case.id
            return HttpResponseRedirect(reverse('job_main', args=[job_id]))
    else:   
        form = CLForm
        if 'submitted' in request.GET:
            submitted = True 
    return render(request, 'JAB_Main/cl_add.html', {'form':form, 'submitted':submitted})

@login_required
def cl_update(request, cl_id):
    current_user = request.user
    cl_case = CoverLetter.objects.get(pk=cl_id, user=current_user)
    form = CLForm(request.POST or None, instance=cl_case)
    if form.is_valid():
        form.save()
        job_id = cl_case.job.id
        return HttpResponseRedirect(reverse('job_main', args=[job_id]))

    return render(request, 'JAB_Main/cl_update.html', {
        'cl_case':cl_case,
        'form':form
    })

@login_required
def cl_delete(request, cl_id):
    current_user = request.user
    cl_case = CoverLetter.objects.get(pk=cl_id, user=current_user) 
    job_id = cl_case.job.id
    cl_case.delete()
    return HttpResponseRedirect(reverse('job_main', args=[job_id])) 

@login_required
def cl_download(request, cl_id):
    current_user = request.user
    cl_case = CoverLetter.objects.get(pk=cl_id, user=current_user) 
    buf = io.BytesIO()
    canvas_case = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    canvas_case.setFont('Helvetica', 14)
    y_position = inch
    
    canvas_case.drawString(inch, y_position, cl_case.text)
    
    canvas_case.showPage()
    canvas_case.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='CoverLetter.pdf')