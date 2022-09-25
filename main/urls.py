from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create-task', views.create, name='create'),
    path('delete-task/<int:id>', views.delete, name='delete')
]
