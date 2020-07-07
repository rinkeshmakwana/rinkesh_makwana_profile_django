from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birthday = models.DateField()
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=40)
    address = models.TextField()

    def __str__(self):
        return f'{self.user.get_full_name()}'

class Social(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=50)
    site_url = models.URLField(max_length=200)

    def __str__(self):
        return self.site_name


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50)
    progress_value = models.IntegerField(default=0)

    def __str__(self):
        return self.skill_name


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=140)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
