from django.contrib import admin
from .models import Profile, Social, Skill, Contact

# Register your models here.
admin.site.register(Profile)
admin.site.register(Social)
admin.site.register(Skill)
admin.site.register(Contact)