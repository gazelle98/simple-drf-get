from django.urls import path

from summation import views

urlpatterns = [
    path('summation/', views.summation),
]
