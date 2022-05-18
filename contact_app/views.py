from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages



# Create your views here.
def index(request):
    if request.method=="POST":
        prod=Contact()
        prod.name=request.POST.get('name')
        prod.email=request.POST.get('email')
        prod.phone=request.POST.get('phone')
        prod.msg=request.POST.get('msg')

        if len(request.FILES)!=0:
            prod.image=request.FILES['image']
        prod.save()
        messages.success(request,'Data submitted successfully!!')
    return render(request,"index.html")

def clear(request):
    return render(request,'index.html')