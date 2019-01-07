from django.urls import path, include

from .views import home_view, stock_info_view, search_result_view

urlpatterns = [
    path('', home_view, name='stocks'),
    path('company/<str:ticker>/', stock_info_view, name='company'),
    path('company/', search_result_view, name='search'),
]
