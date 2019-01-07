from django.shortcuts import render

from .forms import LoginForm

# Create your views here.
def home_view(request):
    return render(request, 'index.html', {})
