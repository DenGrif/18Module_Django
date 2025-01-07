from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Функция для главной страницы со ссылками
def home(request):
    return render(request, 'second_task/index.html')

def task2_index(request):
    return render(request, 'second_task/index.html')  # Путь к шаблону index.html task2


class ClassView(View):
    def get(self, request):
        return render(request, 'second_task/class_view_template.html')

def function_view(request):
    return render(request, 'second_task/function_view_template.html')


