from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Profile, Course, Question_Conctact, Hire_req, Purchase
from .forms import SignUpForm, ProfileRoleForm, ProfilePicForm, CourseForm, contact_form, Hire_form, H_form
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse
from django.core.mail import send_mail
from .forms_factory import ProductFormFactory
from django.db import transaction
from django.contrib.auth.decorators import user_passes_test


def home(request):
    if request.user.is_authenticated:
        form =CourseForm(request.POST or None, request.FILES or None)
        if request.method == "POST":
            if form.is_valid():
                
                course = form.save(commit=False)
                course.user = request.user
                course.save()
                messages.success(request,("Your Course has been posted!!"))
                return redirect('home')
        courses = Course.objects.all().order_by("-created_at")
        return render(request,'index.html', {"courses" : courses, "form" : form})
    else:
        courses = Course.objects.all().order_by("-created_at")
        return render(request,'index.html', {"courses" : courses})

def select_role(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id = request.user.id)
        profile_user = Profile.objects.get(user__id = request.user.id)

        profile_form= ProfileRoleForm(request.POST or None, request.FILES or None, instance = profile_user)
        if profile_form.is_valid(): 
            profile_user.is_philomath = False
            profile_form.save()

            login(request, current_user)
            messages.success(request, ("You are now a Tutor! Please create a tutor profile"))
            return redirect('update_user')
        return render(request, "role.html",{ 'profile_form':profile_form})
    else:
        messages.success(request, ("You must be logged in to view that page"))
        return redirect('home')



def registration_philomath(request):
    form_user = SignUpForm()
    if request.method =="POST":
        form_user = SignUpForm(request.POST)
        if form_user.is_valid():
            form_user.save()
            username = form_user.cleaned_data['username']
            password = form_user.cleaned_data['password1']
            user1 = authenticate(username = username, password= password) 
            login(request, user1)
            messages.success(request, ("You have succesfully registered.. Welcome!!"))
            return redirect('home')        
            
    return render(request, "registration_philomath.html",{'form_user':form_user})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Have Been Logged Out. Sorry To See You Go"))
    return redirect('home')

def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request,("You have been logged in!!"))
            return redirect('home')
        else:
            messages.success(request,("There was an error logging in Please try again!"))
            return redirect('login_user') 
    else:    
        return render(request, "login.html", {} )
    
def update_user(request):
    if request.user.is_authenticated and request.user.profile.is_tutor:
        current_user = User.objects.get(id = request.user.id)
        profile_user = Profile.objects.get(user__id = request.user.id)

        user_form =SignUpForm(request.POST or None, request.FILES or None, instance = current_user)
        profile_form= ProfilePicForm(request.POST or None, request.FILES or None, instance = profile_user)
        if request.method == "POST":
            if user_form.is_valid() and profile_form.is_valid(): 
                user_form.save()
                profile_form.save()

                login(request, current_user)
                messages.success(request, ("Your profile has been updated"))
                return redirect('home')
        return render(request, "update_user.html",{'user_form':user_form, 'profile_form':profile_form})
    else:
        messages.success(request, ("You are not eligible to enter this page"))
        return redirect('home')
    
def update_philomath(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id = request.user.id)
        profile_user = Profile.objects.get(user__id = request.user.id)
        user_form =SignUpForm(request.POST or None, request.FILES or None, instance = current_user)
        if request.method == "POST":
            if user_form.is_valid() : 
                user_form.save()

                login(request, current_user)
                messages.success(request, ("Your profile has been updated"))
                return redirect('home')
        return render(request, "update_philomath.html",{'user_form':user_form})
    else:
        messages.success(request, ("You must be logged in to view that page"))
        return redirect('home')

def profile(request, pk):
    if request.user.is_authenticated:

        profile = Profile.objects.get(user_id=pk)
        courses = Course.objects.filter(user_id = pk).order_by("-created_at")
        questions = Question_Conctact.objects.filter(user_id=pk).order_by("-created_at")
        hire_reqs = Hire_req.objects.filter(user_id=pk).order_by("-created_at")
        q_form = contact_form(request.POST or None)
        hire_form = Hire_form(request.POST or None)
        course_form =CourseForm(request.POST or None, request.FILES or None)

        #post form logic
        if request.method == "POST":

            if course_form.is_valid():
                course = course_form.save(commit=False)
                course.user = request.user
                course.save()
                messages.success(request, ("New Course have been created!"))
                return redirect(request.META.get("HTTP_REFERER"))
            #get current user ID
            if q_form.is_valid():
                Quet = q_form.save(commit=False)

                Quet.user = profile.user
                Quet.save()
                messages.success(request, ("Your question have been submitted!! Tutor may reply you through email."))
                return redirect(request.META.get("HTTP_REFERER"))
            
            elif hire_form.is_valid():
                hire = hire_form.save(commit=False)
                hire.user = profile.user
                hire.save()
                messages.success(request, ("Your request have been submitted!! Tutor may reach out you directly via email!! "))
                return redirect(request.META.get("HTTP_REFERER"))
            
            current_user_profile = request.user.profile
            #get form data
           
            #need to save the profile
            current_user_profile.save()

        return render(request,'profile.html',{"profile" : profile, "courses":courses,"questions":questions ,"hire_reqs":hire_reqs, "q_form":q_form, "hire_form":hire_form, "course_form":course_form})
    else:
        messages.success(request,("You must be logged in to use this page"))
        return redirect('home')

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.order_by('user')
        return render(request, 'profile_list.html', {"profiles":profiles})
    
    else:
        messages.success(request,("You must be logged in to use this page"))
        return redirect('home')
    
def search_user(request):
    if request.method == "POST":
        search = request.POST['search']
        #search the database
        searched = User.objects.filter(username__contains = search)
        return render(request, 'search_user.html', {'search':search, 'searched':searched})
    else:
        return render(request, 'search_user.html', {})
    
def search_field(request):
    if request.method == "POST":
        search = request.POST['search']
        #search the database
        searched = Profile.objects.filter(tutor_field__contains = search)
        return render(request, 'search_field.html', {'search':search, 'searched':searched})
    else:
        return render(request, 'search_field.html', {})
    
def edit_course(request, pk):
    if request.user.is_authenticated:
        course = get_object_or_404(Course, id=pk)
        if request.user.username == course.user.username:
            form =CourseForm(request.POST or None, instance=course)
            if request.method == "POST":
                if form.is_valid():
                    course = form.save(commit = False)
                    course.user = request.user
                    course.save()
                    messages.success(request,("Your Course has been updated!!"))
                    return redirect('home')
            else:
                return render(request, "edit_course.html",{'form':form, 'course':course})
                
        else:
            messages.success(request, ("You don't own that course!"))
            return redirect('home')
    else:
        messages.success(request, ("Please Login To Continue"))
        return redirect('home')
    
def delete_course(request, pk):
    if request.user.is_authenticated:
        course = get_object_or_404(Course, id=pk)
        #check to see if you own the meep
        if request.user.username == course.user.username:
            course.delete()
            messages.success(request, ("The Course has been deleted!!"))
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            messages.success(request, ("You don't own that Course!"))
            return redirect('home')
    else:
        messages.success(request, ("Please Login To Continue"))
        return redirect(request.META.get("HTTP_REFERER"))
    
def course_show(request, pk):
    course = get_object_or_404(Course, id=pk)
    useremail = request.user.email
    link = course.course_link
    host = request.get_host()
    paypal_checkout = {
        'business' : settings.PAYPAL_RECIEVER_EMAIL,
        'amount' : course.course_price,
        'item_name':course.course_name,
        'invoice':uuid.uuid4(),
        'currency_code':'CAD',
        'notify_url':f"http://{host}{reverse('paypal-ipn')}",
        'return_url':f"http://{host}{reverse('purchase_course', kwargs={'pk':pk})}",
        'cancel_url':f"http://{host}{reverse('home')}"
    }

    paypal_payment = PayPalPaymentsForm(initial = paypal_checkout)

    if course:
        return render(request, "show_course.html",{'course':course, 'paypal_payment':paypal_payment})
    else:
        messages.success(request, ("That course does not exist"))
        return redirect('home')

@user_passes_test(lambda u: u.is_authenticated)
def purchase_course(request, pk):
    if request.user.is_authenticated:

        course = get_object_or_404(Course, pk=pk)
        purchase = Purchase.objects.create(user=request.user, course=course)
        # Send email to the user
        subject = f"Course Purchased: {course.course_name}"
        message = f"Thank you for purchasing {course.course_name}! Here is the link to your course: {course.course_link}"  # Replace 'link' with the actual field name
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [request.user.email]
        send_mail(subject, message, from_email, to_email, fail_silently=True)
        return render(request, 'course_give.html', {'course': course})
    else:
        messages.success(request, ("Please Login To Continue"))
        return redirect('home')
    

def delete_question(request, pk):
    if request.user.is_authenticated:
        
        question = get_object_or_404(Question_Conctact, id=pk)
        #check to see if you own the meep
        if request.user.username == question.user.username:
            question.delete()
            messages.success(request, ("The Question has been deleted!!"))
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            messages.success(request, ("You don't own that Question!"))
            return redirect('home')
    else:
        messages.success(request, ("Please Login To Continue"))
        return redirect(request.META.get("HTTP_REFERER"))
    
def delete_hirereq(request, pk):
    if request.user.is_authenticated:
        
        hire_req = get_object_or_404(Hire_req, id=pk)
        #check to see if you own the meep
        if request.user.username == hire_req.user.username:
            hire_req.delete()
            messages.success(request, ("The Hire request has been deleted!!"))
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            messages.success(request, ("You don't own that Hire Request!"))
            return redirect('home')
    else:
        messages.success(request, ("Please Login To Continue"))
        return redirect(request.META.get("HTTP_REFERER"))
    

def h_form(request):
    course_form =CourseForm(request.POST or None, request.FILES or None)
    h_form_instance = ProductFormFactory(request.POST or None)
    if request.method == "POST":
            if h_form_instance.is_valid():
                h_form = ProductFormFactory(request.POST or None, commit=False)
                h_form.user = request.user
                h_form.save()
                messages.success(request, ("New Course have been created!"))
                return redirect(request.META.get("HTTP_REFERER"))

            return render(request,'profile.html',{})

            
    else:
        messages.success(request,("You must be logged in to use this page"))
        return redirect(request.META.get("HTTP_REFERER"))
