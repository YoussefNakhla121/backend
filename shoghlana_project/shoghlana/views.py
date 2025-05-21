from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from .models import Jobs, PostedJobs
from .models import Users
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'shoghlana/index.html')

def home(request):
    return render(request, 'shoghlana/home.html')

def about(request):
    return render(request, 'shoghlana/about.html')


def search(request):

    
    context = {
        'jobs': Jobs.objects.all(),
    }
    return render(request, 'shoghlana/Search_page.html', context)


def filter_jobs(request):
    title = request.GET.get("title", "")
    min_exp = request.GET.get("min_exp", "")
    max_exp = request.GET.get("max_exp", "")
    job_type = request.GET.get("job_type", "")

    jobs = Jobs.objects.all()

    if title:
        jobs = jobs.filter(title__icontains=title)

    if min_exp:
        jobs = jobs.filter(years_of_experience__gte=int(min_exp))

    if max_exp:
        jobs = jobs.filter(years_of_experience__lte=int(max_exp))

    if job_type and job_type != "All":
        jobs = jobs.filter(job_type=job_type)

    job_data = [{
        "id": job.id,
        "title": job.title,
        "company": job.company,
        "experience": job.years_of_experience,
        "type": job.job_type,
        "description": job.description,
        "status": job.status,
    } for job in jobs]

    return JsonResponse({"jobs": job_data})

@login_required
def job_details(request, job_id):
    job = Jobs.objects.get(id=job_id)
    already_applied = False
    if request.user.is_authenticated:
        already_applied = job.application_set.filter(user=request.user).exists()
    context = {
        'job': job,
        'already_applied': already_applied,
    }
    return render(request, 'shoghlana/job_details.html', context)

def apply_job(request, job_id):
    job = Jobs.objects.get(id=job_id)
    user = request.user
    job.application_set.create(user=user)
    return HttpResponseRedirect('/Search_page/')

def applied_jobs(request):
    applied_jobs = request.user.application_set.all()
    jobs = [applied_job.job for applied_job in applied_jobs]
    context = {
        'applied_jobs': jobs,
    }
    return render(request, 'shoghlana/applied_jobs.html', context)

def applied_job_details(request, job_id):
    job = Jobs.objects.get(id=job_id)
    context = {
        'job': job,
    }
    return render(request, 'shoghlana/applied_job_details.html', context)

@login_required
def add_job(request):
    return render(request, 'shoghlana/add_job.html')

def submit_job(request):
    title = request.POST.get('job_title')
    company = request.POST.get('company_name')
    years_of_experience = request.POST.get('years_of_experience')
    job_type = request.POST.get('job_type')
    description = request.POST.get('job_description')
    status = request.POST.get('status')
    salary = request.POST.get('salary')

    job = Jobs.objects.create(
        title=title,
        company=company,
        years_of_experience=years_of_experience,
        job_type=job_type,
        description=description,
        status=status,
        salary=salary,
    )
    job.save()

    posted_job = PostedJobs.objects.create(
        user=request.user,
        job=job,
        status=status
    )
    posted_job.save()
    return HttpResponseRedirect('/Search_page/')

def posted_jobs(request):
    posted_jobs = request.user.postedjobs_set.all()
    jobs = [posted_jobs.job for posted_jobs in posted_jobs]
    context = {
        'posted_jobs': jobs,
    }
    return render(request, 'shoghlana/posted_jobs.html', context)

def edit_job(request, job_id):
    job = Jobs.objects.get(id=job_id)
    context = {
        'job': job,
    }
    return render(request, 'shoghlana/edit_job.html', context)

def submit_edit_job(request, job_id):
    job = Jobs.objects.get(id=job_id)
    title = request.POST.get('job_title')
    company = request.POST.get('company_name')
    years_of_experience = request.POST.get('years_of_experience')
    job_type = request.POST.get('job_type')
    description = request.POST.get('job_description')
    status = request.POST.get('status')
    salary = request.POST.get('salary')

    job.title = title
    job.company = company
    job.years_of_experience = years_of_experience
    job.job_type = job_type
    job.description = description
    job.status = status
    job.salary = salary
    job.save()

    return HttpResponseRedirect('/profile/posted_jobs/')

def delete_job(request, job_id):
    job = Jobs.objects.get(id=job_id)
    job.delete()
    return HttpResponseRedirect('/profile/posted_jobs/')

@login_required
def profile(request):
    return render(request, 'shoghlana/profile.html')

def edit_profile(request):
    return render(request, 'shoghlana/edit_profile.html')

def submit_edit_profile(request):
    user = request.user
    name = request.POST.get('name')
    location = request.POST.get('location')
    occupation = request.POST.get('occupation')
    skills = request.POST.get('skills')
    experience = request.POST.get('experience')

    user.Name = name
    user.location = location
    user.occupation = occupation
    user.skills = skills
    user.years_of_experience = experience
    user.save()

    return HttpResponseRedirect('/profile/')

def signup(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    country = request.POST.get('country')
    user_type = request.POST.get('user-type')
    admin_company = request.POST.get('admin_company')
    user = Users.objects.create_user(username=username, email=email, password=password, country=country, type=user_type, admin_company=admin_company)
    user.save()
    login(request, user)
    return redirect('/home/')

def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user_type = request.POST.get('user-type')
    user = authenticate(request, username=username, password=password)
    if user is not None and user.type == user_type:
        login(request, user)
        return HttpResponseRedirect('/home/')
    else:
        return render(request, 'shoghlana/index.html', {'error': 'Invalid credentials'})
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def view_applicants(request, job_id):
    job = Jobs.objects.get(id=job_id)
    # Check if the user is an admin and owns this job
    if request.user.type == 'Admin' and job.postedjobs_set.filter(user=request.user).exists():
        applications = job.application_set.all()
        context = {
            'job': job,
            'applications': applications,
        }
        return render(request, 'shoghlana/view_applicants.html', context)
    return HttpResponseRedirect('/profile/posted_jobs/')
