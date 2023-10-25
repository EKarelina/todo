from django.shortcuts import render
from .models import Task
from .models import Kategorii


def index(request):
    result = ""

    kateg = ""
    for a in Kategorii.objects.all():
        kateg += a.kategoriya
    return render(
        request,
        "mainpage/index.html",
        # Kонтекст передаваемых переменных
        {"Задачи": Task.objects.all(), "Категории": kateg}

    )
