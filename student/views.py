from django.shortcuts import render
from django.http import HttpResponse
from .models import data
def home(request):
    mymembers=data.objects.all()
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        data.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender
        )
        return HttpResponse("Data added successfully.<a href='/firs'>Go back</a>")
    return render(request,'first.html',{'mymembers':mymembers})
