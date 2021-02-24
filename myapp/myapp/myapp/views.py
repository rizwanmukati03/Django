from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    
    return render(request,'index.html')

def fullname(request):
    fname = request.Get.get('firstname')
    lname = request.Get.get('lastname')

    fullname = f"{fname} {lname}"
    data= {'fullname':fullname}

    return render(request, 'index.html', data)