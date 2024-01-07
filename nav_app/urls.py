from django.urls import path
from . import views
urlpatterns = [
    path('booktaxi/', views.book_taxi, name='book_taxi'),
]

