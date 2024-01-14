from django.shortcuts import render
from django.template import loader

# Create your views here.

def website(request, user_id):
    # load user data etc.
    # data = 
    # context = {
    #     "latest_question_list": data,
    # }
    context = None
    
    return render(request, "cms_core/index.html", context)