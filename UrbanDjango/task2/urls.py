from django.urls import path
from .views import ClassView, function_view, task2_index

urlpatterns = [
    path('index/', task2_index, name='task2_index'),
    path('class-view/', ClassView.as_view(), name='class_view'),
    path('function-view/', function_view, name='function_view'),
]