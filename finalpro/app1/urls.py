
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home , name="home"),
    path('register', views.registration_philomath , name="register"),
    path('logout_user', views.logout_user , name="logout_user"),
    path('login_user', views.login_user , name="login_user"),
    path('select_role', views.select_role , name="select_role"),
    path('update_user', views.update_user , name="update_user"),
    path('update_philomath', views.update_philomath , name="update_philomath"),
    path('profile/<int:pk>',views.profile, name='profile'),
    path('profile_list/',views.profile_list, name='profile_list'),
    path('search_user/',views.search_user, name='search_user'),
    path('search_field/',views.search_field, name='search_field'),
    path('delete_question/<int:pk>',views.delete_question, name='delete_question'),
    path('delete_hirereq/<int:pk>',views.delete_hirereq, name='delete_hirereq'),
    path('edit_course/<int:pk>',views.edit_course, name='edit_course'),
    path('delete_course/<int:pk>',views.delete_course, name='delete_course'),
    path('course_show/<int:pk>',views.course_show, name='course_show'),
    path('purchase_course/<int:pk>',views.purchase_course, name='purchase_course'),    
]
