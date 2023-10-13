from django.shortcuts import render, redirect
from.models import *
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def index(request):
    return render(request,'index.html')

def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        em = request.POST['email']
        pwd = request.POST['pwd']
        try:
          user = User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
          EmployeeDetail.objects.create(user = user,empcode=ec)
          EmployeeExperience.objects.create(user = user)
          EmployeeEducation.objects.create(user = user)
          #empcode holds on EmployeeDetail Model
          error = "no"
        except:
            error = "yes" 
           
        
    return render(request,'registration.html',locals())

def emp_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        if user:
            login(request,user)
            error = "no"
        else:
            error ="yes"
    return render(request,'emp_login.html',locals())

def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login') 
    return render(request,'emp_home.html')

def Logout(request):
    logout(request)
    return redirect('index')



def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')    
    error = ""
    user = request.user
    employee = EmployeeDetail.objects.get(user = user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate'] 
        gender = request.POST['gender'] 
        
        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = ec
        employee.empdept = dept
        employee.designation = designation 
        employee.contact = contact
        employee.gender = gender
        
        if jdate:
           employee.joiningdate = jdate 
        
              
        try:
            employee.save()
            employee.user.save()
            
            error = "no"
        except:
            error = "yes"
           
        
    return render(request,'profile.html',locals())

def admin_login(request):
    return render(request,'admin_login.html')



def my_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')    
    error = ""
    user = request.user
    experience = EmployeeExperience.objects.get(user = user)
        
    return render(request,'myexperience.html',locals())

def edit_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')    
    error = ""
    user = request.user
    experience = EmployeeExperience.objects.get(user = user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate'] 
        gender = request.POST['gender'] 
        
        experience.user.first_name = fn
        experience.user.last_name = ln
        experience.empcode = ec
        experience.empdept = dept
        experience.designation = designation 
        experience.contact = contact
        experience.gender = gender
    
        try:
            experience.save()
            error = "no"
        except:
            error = "yes"
           
        
    return render(request,'edit_experience.html',locals())