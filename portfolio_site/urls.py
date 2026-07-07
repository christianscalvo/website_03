from django.contrib import admin
from django.urls import path

from pages import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("projects/", views.projects, name="projects"),
    path("projects/mining-laboratory-dashboard/", views.mining_lab_dashboard, name="mining_lab_dashboard"),
    path("projects/koa-campgrounds-dashboard/", views.koa_campgrounds_dashboard, name="koa_campgrounds_dashboard"),
    path("about/", views.about, name="about"),
    path("resume/", views.resume, name="resume"),
]