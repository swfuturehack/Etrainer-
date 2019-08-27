from django.db import models
from app.models import User



STATUS = (
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Doctor', 'Doctor'),
    ('Professor', 'Professor'),
)

# Create your models here.

# Create your models here.
class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS)
    profilepic = models.ImageField(upload_to = 'instructor/', blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.user.username

    @property
    def image_url(self):
        if self.profilepic:
            return self.profilepic.url
        else:
            return r"/static/user.png"
