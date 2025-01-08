from django.shortcuts import render


def home(request):
    return render(request, 'fourth_task/index.html')


def store(request):
    context = {'games': ["Описание игры 1", "Описание игры 2", "Описание игры 3"]}
    return render(request, 'fourth_task/store.html', context)


def cart(request):
    # Имитация пустой корзины
    cart_items = []

    # тестовые данные для тестирования
    # cart_items = ['Товар 1', 'Товар 2']

    is_empty = not bool(cart_items)

    context = {
        'cart_items': cart_items,
        'is_empty': is_empty
    }

    return render(request, 'fourth_task/cart.html', context)

# from django.shortcuts import render
#
# def home(request):
#     return render(request, 'fourth_task/index.html')
#
# def store(request):
#     context = {'games': ["Описание игры 1", "Описание игры 2"]}
#     return render(request, 'fourth_task/store.html', context)
#
# def cart(request):
#     return render(request, 'fourth_task/cart.html')
