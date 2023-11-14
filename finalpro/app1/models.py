from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save    

class Course(models.Model):
    user = models.ForeignKey( User, related_name="course", on_delete=models.DO_NOTHING)
    course_name = models.CharField(max_length=50)
    course_price = models.FloatField(default=0.00)
    des= models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="course_like", blank=True)
    course_image = models.ImageField(null = True, blank = True, upload_to="images2/")
    course_link = models.CharField(max_length=500, default="")
    #keep count of like
    def number_of_likes(self):
        return self.likes.count()         

    def __str__(self):
        return(f"{self.user}"
               f"({self.created_at:%y-%m-%d %H:%M}): "
               f"{self.des}..."
               f"{self.course_image}"
               )

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(f"{self.user}"
               f"{self.course}"
               f"{self.purchase_date}"
               )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    follows = models.ManyToManyField("self",
                                     related_name="followed_by",
                                     symmetrical=False,
                                     blank=True)
    is_philomath = models.BooleanField('philomath status', null=True, blank = True, default = True)
    is_tutor = models.BooleanField('tutor status',null=True, blank = True)
    profile_image = models.ImageField(null = True, blank = True, upload_to="images/")
    tutor_field = models.CharField(max_length = 50)
    profile_bio = models.CharField(null=True, blank = True, max_length=1000)
    homepage_link = models.CharField(null=True, blank = True, max_length=500)
    facebook_link = models.CharField(null=True, blank = True, max_length=500)
    instagram_link = models.CharField(null=True, blank = True, max_length=500)
    linkedin_link = models.CharField(null=True, blank = True, max_length=500)

    def __str__(self):
        return self.user.username



#create  profile when new user is created
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile= Profile(user = instance)
        user_profile.save()

post_save.connect(create_profile, sender = User)


class Question_Conctact(models.Model):
    user = models.ForeignKey( User, related_name="Question", on_delete=models.DO_NOTHING)
    alt_email = models.CharField(max_length=100)
    question = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    #keep count of like
    def __str__(self):
        return(f"{self.user}"
               f"({self.created_at:%y-%m-%d %H:%M}): "
               f"{self.question}..."
               f"{self.alt_email}"
               )
    
class Hire_req(models.Model):
    user = models.ForeignKey( User, related_name="Request", on_delete=models.DO_NOTHING)
    your_email = models.CharField(max_length=100)
    Request = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return(f"{self.user}"
               f"({self.created_at:%y-%m-%d %H:%M}): "
               f"{self.Request}..."
               f"{self.your_email}"
               )
    
