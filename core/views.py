from django.shortcuts import render
from .models import Profile, Social, Skill
from .forms import ContactForm

# Create your views here.
def profile_view(request):
    user = Profile.objects.get(id=1)
    socials = Social.objects.filter(user__id=user.id)
    skills = Skill.objects.filter(user__id=user.id)
    form = ContactForm()
    context = {
        'user': user,
        'socials': socials,
        'skills': skills,
        'form': form,
    }
    return render(request, 'index.html', context)