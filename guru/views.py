from django.shortcuts import render
from guru.models import Student
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    student=Student.objects.all().values()
    if request.method == 'POST':
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        user = User.objects.create_user(email, email, pass1)
        user.save()
        
    
    

    return render(request,'index.html',{'student':student})
