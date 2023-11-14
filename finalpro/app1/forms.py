from django import forms
from .models import User,Profile, Course, Question_Conctact, Hire_req
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from abc import ABC, abstractmethod


class ProfileRoleForm(forms.ModelForm):
    is_tutor = forms.BooleanField(help_text='<span class="form-text text-muted"><small>Click here to become a Tutor. This action is irrevesible!!!</small></span>')

    class Meta:
        model= Profile
        fields = ( 'is_tutor', )

class ProfilePicForm(forms.ModelForm):
    profile_image = forms.ImageField(label="Profile Picture")
    tutor_field = forms.CharField(required = True, label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Field of Teaching'}))
    profile_bio = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Profile Bio'}))
    homepage_link = forms.CharField(required = False, label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Website Link'}))
    facebook_link = forms.CharField(required = False, label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Facebook Link'}))
    instagram_link = forms.CharField(required = False, label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Instagram Link'}))
    linkedin_link = forms.CharField(required = False, label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'LinkedIn Link'}))

    class Meta:
        model= Profile
        fields = ('profile_image', 'profile_bio','tutor_field', 'homepage_link', 'facebook_link', 'instagram_link', 'linkedin_link' )


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'first_name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'last_name'}))
    

    class Meta:
        model =User
        fields = ('username', 'first_name','last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class CourseForm(forms.ModelForm):
    course_image = forms.ImageField(label="Course Picture", required = False)
    course_name = forms.CharField(required = True, label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name Of Course'}))
    course_link = forms.CharField(required = True, label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Course Link'}))
    course_price = forms.FloatField(required = True, label="", widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Course Price'}))
    des = forms.CharField(required= True , 
                           widget = forms.widgets.Textarea(
                               attrs={
                                   "placeholder":"Enter your Course Description here!!",
                                   "class":"form-control",
                               }
                           ),
                           label="",
                           )
    class Meta:
        model = Course
        fields = ('course_name', 'des', 'course_image','course_link','course_price' )
        exclude = ("user", "likes",)

class contact_form(forms.ModelForm):
    alt_email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your email...'}))
    question = forms.CharField(required= True , widget = forms.widgets.Textarea(attrs={"placeholder":"Enter your Question here!!","class":"form-control",}),label="",)
    
    class Meta:
        model = Question_Conctact
        fields = ('alt_email', 'question')
        exclude = ("user",)


class Hire_form(forms.ModelForm):
    your_email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your email...'}))
    Request = forms.CharField(required= True , widget = forms.widgets.Textarea(attrs={"placeholder":"Give a short intro about yourself!!","class":"form-control",}),label="",)
    
    class Meta:
        model = Hire_req
        fields = ('your_email', 'Request')
        exclude = ("user",)

class H_form(forms.Form):
    your_email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your email...'}))
    Request = forms.CharField(required= True , widget = forms.widgets.Textarea(attrs={"placeholder":"Give a short intro about yourself!!","class":"form-control",}),label="",)
 