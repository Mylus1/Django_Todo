from django.urls import path

from . import views

urlpatterns = [
    path('todos/', views.Todo_FullList.as_view(), name='Todo-List'),
    path('todos/<pk>/', views.Todo_Edit.as_view(), name='Todo-Edit'),
    path('', views.index, name='index'),
    path('create', views.create, name='form'),
    path('sign_up', views.sign_up, name='sign_up')
]

