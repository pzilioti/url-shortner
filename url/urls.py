from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('short/<str:url>/', views.get_short_url, name='short'),
	path('long/<str:url>/', views.get_long_url, name='long'),
	path('<str:url>/', views.redirect_url, name='redirect'),
]