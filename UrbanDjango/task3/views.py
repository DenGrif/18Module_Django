from django.shortcuts import render

def home(request):
    return render(request, 'third_task/index.html')

def store(request):
    items = {
        'Игра 1': 'Описание игры 1',
        'Игра 2': 'Описание игры 2',
        'Игра 3': 'Описание игры 3',
    }
    return render(request, 'third_task/store.html', {'items': items})

def cart(request):
    return render(request, 'third_task/cart.html')
