import todo  # Это название вашего проекта
from django.shortcuts import render
from .models import Task
from .models import Kategorii
from .models import Goods


def get_menu(active):
    result = []
    for elem in todo.urls.navset:
        if elem['url'] == active:
            elem['active'] = True
        result.append(elem)
    return result


def index(request):
    result = ""

    kateg = ""
    for a in Kategorii.objects.all():
        kateg += a.kategoriya

    return render(
        request,
        "mainpage/index.html",

        # Kонтекст передаваемых переменных
        {
            "Задачи": Task.objects.all(), "Категории": kateg,
            "navset": get_menu("/")

        }
    )


def pokupki(request):

    result = ""

    tovary = ""
    for x in Goods.objects.all():
        tovary += x.namegoods

    return render(
        request,
        "mainpage/index2.html",

        # Kонтекст передаваемых переменных
        {

            "Товары": Goods.objects.all(),
            "navset": get_menu("/shopping")

        }
    )
