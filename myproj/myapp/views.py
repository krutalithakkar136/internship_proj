from django.shortcuts import render
from myapp.models import Practice

# Create your views here.
def signup(request):
    print('request.method: ', request.method)
    if request.method=="POST":
        print('request.POST[]: ', request.POST['name'])
        Practice.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            address=request.POST['address'],
        )
        user=Practice.objects.all()
        return render(request,'signup.html',{'user':user})
    else:
        return render(request,'signup.html')
    
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')

def shop(request):
    return render(request,'shop.html')

def index(request):
    return render(request,'/')