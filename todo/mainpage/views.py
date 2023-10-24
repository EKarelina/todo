from django.shortcuts import render
from .models import Task


def index(request):
    result = ""
    for t in Task.objects.all():
        result += t.description
    kateg = ""    
    for a in Kategorii.objects.all():
        kateg += a.kategoriya    
    return render(
        request,
        "mainpage/index.html",
        {"Задачи": result, "Категории": kateg}
   
    )



from .models import Kategorii


#def index(request):

 #   return render(
 #       request,
 #       "mainpage/index.html",
 #       {"zadachi":Kategorii.objects.all()}
   # )