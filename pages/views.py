from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")


def projects(request):
    return render(request, "pages/projects.html")

def mining_lab_dashboard(request):
    return render(request, "pages/projects/mining_lab_dashboard.html")

def koa_campgrounds_dashboard(request):
    return render(request, "pages/projects/koa_campgrounds_dashboard.html")

def about(request):
    return render(request, "pages/about.html")


def resume(request):
    return render(request, "pages/resume.html")