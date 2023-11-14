from django.contrib import admin
from .models import User, Profile, Course, Question_Conctact, Hire_req, Purchase
from django.contrib.auth.models import Group, User

#unregister group
admin.site.unregister(Group)

#mix profile info into user info

class ProfileInline(admin.StackedInline):
    model = Profile


#extend user model
class UserAdmin(admin.ModelAdmin):
    model = User
    #just display username on admin page
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.unregister(User)

admin.site.register(User, UserAdmin)
# Register your models here.
admin.site.register(Course)

admin.site.register(Purchase)

admin.site.register(Question_Conctact)

admin.site.register(Hire_req)
