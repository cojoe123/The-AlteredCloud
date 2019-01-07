from django.shortcuts import render

from . import services

# Create your views here.
def repo_view(request):
    projects = services.get_repos()
    return render(request, 'github/repos.html', {'info': projects} )