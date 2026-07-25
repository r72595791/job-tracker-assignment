from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Count
from .models import JobApplication
from .forms import JobApplicationForm

def home_view(request):
    total_apps = JobApplication.objects.count()
    status_counts = JobApplication.objects.values('status').annotate(count=Count('status'))
    
    counts = {
        'Applied': 0,
        'Interview': 0,
        'Offer': 0,
        'Accepted': 0,
        'Rejected': 0,
    }
    for item in status_counts:
        counts[item['status']] = item['count']

    context = {
        'total_apps': total_apps,
        'counts': counts,
    }
    return render(request, 'home.html', context)

def job_list(request):
    jobs = JobApplication.objects.all().order_by('-created_at')
    return render(request, 'jobs/list.html', {'jobs': jobs})

def job_create(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Job application created successfully!")
            return redirect('job_list')
    else:
        form = JobApplicationForm()
    return render(request, 'jobs/create.html', {'form': form})

def job_update(request, id):
    job = get_object_or_404(JobApplication, id=id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, "Job application updated successfully!")
            return redirect('job_list')
    else:
        form = JobApplicationForm(instance=job)
    return render(request, 'jobs/update.html', {'form': form, 'job': job})

def job_delete(request, id):
    job = get_object_or_404(JobApplication, id=id)
    if request.method == 'POST':
        job.delete()
        messages.success(request, "Job application deleted successfully!")
        return redirect('job_list')
    return render(request, 'jobs/delete.html', {'job': job})

def job_detail(request, id):
    job = get_object_or_404(JobApplication, id=id)
    return render(request, 'jobs/detail.html', {'job': job})
