from django.shortcuts import render
from django.template import loader
from .models import Section

# Create your views here.

def website(request, user_id):
    # load user data etc.
    sections = Section.objects.filter(user_id=user_id, visible=True).all()
    # data = 
    context = {
        "sections": sections,
    }
    
    return render(request, "cms_core/index.html", context)