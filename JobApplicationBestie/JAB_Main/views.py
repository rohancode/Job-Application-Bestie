from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import JobForm
from django.http import HttpResponseRedirect
from .models import Job


def home(request):
    return render(request, 'JAB_Main/home.html', {})

def job_add(request):
    submitted = False
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('job_add?submitted=True')
    else:   
        form = JobForm
        if 'submitted' in request.GET:
            submitted = True 
    return render(request, 'JAB_Main/job_add.html', {'form':form, 'submitted':submitted})

def jobs(request):
    job_all = Job.objects.all()
    return render(request, 'JAB_Main/jobs.html', {
        'job_all':job_all
    })


def job_main(request, job_id):
    job_case = Job.objects.get(pk=job_id) 
    return render(request, 'JAB_Main/job_main.html', {
        'job_case':job_case
    })
    
def job_update(request, job_id):
    job_case = Job.objects.get(pk=job_id) 
    form = JobForm(request.POST or None, instance=job_case)
    if form.is_valid():
        form.save()
        return redirect('jobs')

    return render(request, 'JAB_Main/job_update.html', {
        'job_case':job_case,
        'form':form
    })