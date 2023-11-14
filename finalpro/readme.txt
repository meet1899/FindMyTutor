{% extends 'base.html' %}
{% load static %}
{% block content %}

<div class="container text-center">
  <div class="row">
      <div class ="col-8">

{% for course in courses %}
<div class="alert alert-dark" role="alert">
  <div class="container">
    <div class="row">
      <div class="col-1">
        {% if course.course_image %}
        <img src="{{course.course_image.url}}" width =50 height=50 class="rounded-circle" alt = "{{profile.user.username}}">

        {% else %}
        <img src = "{% static 'images/default1.png' %}" width =50 height=50 class="rounded-circle" alt = "{{profile.user.username}}">
        {% endif %}

      </div>
      
      <div class="col-10">
        <strong> {{course.course_name}} </strong><br/>
  <!-- <strong>{{ course.des }}</strong><br/> -->
  <small class="text-muted">
      {{course.created_at}} by 
      @{{course.user.username}}
      &nbsp;&nbsp; {{course.number_of_likes}} 

       &nbsp;&nbsp;
  </small>
  <a href="{% url 'course_show' course.id %}">Show</a>
  </div>
  <br/><br/></div></div></div>  
  {% endfor %}

  </div>
  {% if form and user.profile.is_tutor %}
  <div class ="col-4">
  <div class="card">
    <div class="card-header">
      Upload A New Course!!
    </div>
    <div class="card-body">
      <br/>
    <form method="POST" action="" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p}}
        <button type="submit" class="btn btn-outline-secondary">Upload Course!</button>
      </form>
    </div>
  </div>
</div>

  
    
      {% endif %}
 


{% endblock %}



//using ratelimit to limit the number of questions one can ask


class Hire_form(forms.ModelForm):
    your_email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your email...'}))
    Request = forms.CharField(required= True , widget = forms.widgets.Textarea(attrs={"placeholder":"Give a short intro about yourself!!","class":"form-control",}),label="",)
    
    class Meta:
        model = Hire_req
        fields = ('your_email', 'Request')
        exclude = ("user",)