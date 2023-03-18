from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('booktaxi/', views.book_taxi, name='book_taxi'),
]

