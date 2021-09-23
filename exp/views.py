from django.shortcuts import render, HttpResponse
import requests
from . import models

# Create your views here.

def home(request):

    # p = Info.objects.all().filter(
    #     port
    # )
    #
    # if p is 525:
    #     response = requests.get('http://127.0.0.1:8000/ontact/').json()
    #     return render(request, 'home.html', {'response':response})
    # else:
    #     False

    response = requests.get('http://127.0.0.1:8000/ontact/').json()
    return render(request, 'home.html', {'response': response})
    # print(response.status_code)
    # a == response.status_code
    # if response.status_code == 200:
    #     return HttpResponse("success")
    #
    # else:
    #     return HttpResponse("error")




