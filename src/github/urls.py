from django.urls import path

from .views import repo_view 

urlpatterns = [
    path('', repo_view, name='github'),
]