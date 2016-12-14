from django.shortcuts import render

# Create your views here.
import users


def test (request):
    contex ={}
    m="hello word!"
    contex["textValue"]=m
    return render(request,'users.html',contex);
