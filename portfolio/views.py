from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    """
    Displays home page for the user when requested
    """
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})
