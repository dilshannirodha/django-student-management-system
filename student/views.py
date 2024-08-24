from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages

# Create your views here.

def  home(request):
    std = Student.objects.all()
    return render(request, "student/home.html",{'std':std})

def student_add(request):
    if request.method == 'POST':
        #retrieve user inputs
        regnumber = request.POST['regnumber']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        email = request.POST['email']
        nic = request.POST['nic']
        address = request.POST['address']
        gender = request.POST['gender']

        #create object model
        student = Student(
            regnumber=regnumber,
            firstname=firstname,
            lastname=lastname,
            phone=phone,
            email=email,
            nic=nic,
            address=address,
            gender=gender
        )
        student.save()
        messages.success(request, "Student created successfully.")


    return render(request, "student/add-student.html",{})



def student_delete(request,regnumber):
    
    s=Student.objects.get(regnumber=regnumber)
    s.delete()
    messages.success(request, "Student deleted successfully.")

    return redirect('/home')



def student_update(request, regnumber):
    std_update = Student.objects.get(regnumber = regnumber)
    return render(request, 'student/update-student.html', {'std_update': std_update})

def update(request,regnumber):
     if request.method == 'POST':
        
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        email = request.POST['email']
        nic = request.POST['nic']
        address = request.POST['address']
        gender = request.POST['gender']

        std = Student.objects.get(regnumber = regnumber)
        std.firstname = firstname
        std.lastname = lastname
        std.phone = phone
        std.email = email
        std.nic = nic
        std.address = address
        std.gender = gender

        std.save()
        return redirect('/home')
