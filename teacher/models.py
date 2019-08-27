from django.db import models
from django.contrib.auth.models import AbstractUser
from app.models import *
from datetime import datetime, timedelta


def get_deadline():
    return datetime.today() + timedelta(days=30)

def get_expire():
    return datetime.today() + timedelta(days=365)




class Cadre(models.Model):
    name = models.CharField("Cadre", max_length=50)    
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField("HAPPS", max_length=50)    
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 




class TeacherProfile(models.Model):

    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
       
    )

    MARRIAGE = (
        ('Married', 'Married'),
        ('Single', 'Single'),
        ('Divorced', 'Divorced'),
       
    )
        
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=120)
    address = models.CharField(max_length=250)
    gender = models.CharField(max_length=25, choices=GENDER, default='Male')
    state = models.CharField(max_length=25)
    local = models.CharField(max_length=25)
    status = models.CharField(max_length=25, choices=MARRIAGE, default='Married')
    profilepic = models.ImageField(upload_to = 'profile/', blank=True)
    valid = models.ImageField(upload_to='identification/%Y/%m/%d', blank=True)
    appointment = models.ImageField(upload_to='identification/%Y/%m/%d', blank=True)
    level = models.ForeignKey(Level, related_name="level", on_delete=models.CASCADE)
    cadre = models.CharField(max_length=50, null=True)
    slug = models.SlugField(unique=False)
    active = models.BooleanField(default=True)
    process = models.BooleanField(default=False)
    proceed = models.BooleanField(default=False)
    trailperiod = models.DateTimeField(default=get_deadline)
    fullperiod = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ('-created_at',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.storename
    
    

    def save(self, *args, **kwargs):
        value = self.storename
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


# Create your models here.
class TeacherCourse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course, related_name='studentinterest')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.user.username
