from django.shortcuts import render,redirect
from clgapp.models import Course,Student,UserMember
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
import os
# Create your views here.
def index(request):
    return render(request,'home.html')
def ind(request):
    return render(request, 'adminhome.html')
def coursepage(request):
    return render(request, 'course.html')
@login_required(login_url='login1')
def add_course(request):
    if request.method == 'POST':
        course_name = request.POST['course']
        course_fee = request.POST['fee']
        course = Course(course_name=course_name, fee=course_fee)
        course.save()
        return redirect('add_course')
    else:
        courses = Course.objects.all() 
        return render(request, 'course.html', {'courses': courses})
@login_required(login_url='login1')    
def studentpage(request):
    courses = Course.objects.all()
    return render(request, 'student.html', {'courses': courses})
@login_required(login_url='login1')
def add_student(request):
    if request.method == 'POST':
        student_name = request.POST['fullname']
        student_address = request.POST['email']
        student_age = request.POST['age']
        jdate = request.POST['joining_date']
        sel = request.POST.get('sel')
        course1 = Course.objects.get(id=sel)
        student = Student(student_name=student_name, email=student_address, student_age=student_age, joining_date=jdate, course=course1)
        student.save()
        return redirect("add_student")
    
    else:
        courses = Course.objects.all()
        return render(request, 'student.html', {'courses': courses})
@login_required(login_url='login1')
def showstd(request):
    student = Student.objects.all()
    return render(request, 'show.html', {"student": student})
@login_required(login_url='login1')
def edit(request, pk):
    student = Student.objects.get(id=pk)
    courses = Course.objects.all()
    return render(request, 'edit.html', {'student': student, 'courses': courses})
@login_required(login_url='login1')
def editpage(request, pk):
    student = Student.objects.get(id=pk)
    courses = Course.objects.all()

    if request.method == 'POST':
        student.student_name = request.POST['stdname']
        student.email = request.POST['email']
        student.student_age = request.POST['age']
        student.joining_date = request.POST['joindate']
        student.course = Course.objects.get(id=request.POST['sel'])
        student.save()
        return redirect('/showstd')

    return render(request, 'edit.html', {'student': student, 'courses': courses})
@login_required(login_url='login1')
def deletestd(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('showstd')
def usercreate(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_name = request.POST['username']
        emails = request.POST['email']
        pass_word = request.POST['password']
        cpass_word = request.POST['cpassword']
        address = request.POST['address']
        im = request.FILES.get('photo')
        age = request.POST['age']
        phone_number = request.POST['number']
        sel = request.POST.get('sel')
        course1 = Course.objects.get(id=sel)
        if pass_word == cpass_word:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'This username already exists!!!!')
                courses = Course.objects.all()
                return redirect('login1')
            else:
                user = User.objects.create_user(username=user_name, first_name=first_name, last_name=last_name, email=emails, password=pass_word)
                user.save()
                member = UserMember(user=user,course=course1,address=address,age=age,number=phone_number,image=im)
                member.save()
                messages.info(request, 'User created successfully')
        else:
            messages.info(request, 'Password does not match')
            courses = Course.objects.all()
            return redirect('showtcr')

    courses = Course.objects.all()
    return render(request, 'userhome.html', {'courses': courses})
def login1(request):
    if request.method=='POST':
        user_name=request.POST['username']
        pass_word=request.POST['password']
        user=auth.authenticate(username=user_name,password=pass_word)
        if user is not None:
            if user.is_staff:
                login(request, user)  
                return redirect('ind')
            else:
                login(request, user) 
                messages.info(request, f'Welcome {user_name}')
                return render(request, 'userhome.html')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('/')
    return render(request, 'home.html')
def signup(request):
    courses = Course.objects.all()
    return render(request, 'teachersignup.html', {'courses': courses})
def userhome(request,pk):
    member = UserMember.objects.get(id=pk)
    return render(request,'userhome.html',{'member':member})

def edituserpage(request):
    a=request.user.id
    member = UserMember.objects.get(user=a)
    courses = Course.objects.all()
    return render(request, 'edituser.html', {'member': member, 'courses': courses})
@login_required(login_url='login1')
def edituser(request, pk):
    member = UserMember.objects.get(user=pk)
    user = User.objects.get(id=pk)
    courses = Course.objects.all()
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        member.address = request.POST['address']
        if 'image' in request.FILES:
            if member.image:
                os.remove(member.image.path)
            member.image = request.FILES['image']
        member.age = request.POST['age']
        member.number = request.POST['number']
        member.course = Course.objects.get(id=request.POST.get('sel'))
        member.save()
        messages.success(request, 'User details updated successfully')
        return redirect('display')
    return render(request, 'edituser.html', {'member': member, 'courses': courses})
@login_required(login_url='login1')
def showtcr(request):
    member = UserMember.objects.all()
    user = User.objects.all()
    return render(request,'showteacher.html',{'member':member,'user':user})
@login_required(login_url='login1')
def display(request):
    a=request.user.id
    member = UserMember.objects.get(user=a)
    return render(request, 'usercard.html', {'member': member})
@login_required(login_url='login1')
def deletetcr(request, pk):
    member =UserMember.objects.get(user=pk)
    user=User.objects.get(id=pk)
    member.delete()
    user.delete()
    return redirect('showtcr')
@login_required(login_url='login1')
def logout(request):
    auth.logout(request)
    return redirect('index')
