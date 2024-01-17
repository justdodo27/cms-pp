from django.shortcuts import render

from .models import Section, History, CustomUser, Message, Social
from .forms import MessageForm

from itertools import groupby


def categorize_histories(x):
    work = []
    education = []

    for el in x:
        if el.type == 'w':
            work.append(el)
        if el.type == 'e':
            education.append(el)

    return {
        'work': work,
        'education': education
    }


def parse_socials(x):
    socials = []
    for el in x:
        socials.append(el)

    return socials


def website(request, user_id):
    # add message
    message = None
    if request.method == "POST":
        form = MessageForm(request.POST)

        if form.is_valid():
            Message.objects.create(
                name = request.POST['name'],
                email = request.POST['email'],
                subject = request.POST['subject'],
                message = request.POST['message'],
                user_id = CustomUser.objects.get(id=user_id)
            )
            message = f"Your message {request.POST['subject']} sent succesfully."

    # load user data etc.
    sections = Section.objects.filter(user_id=user_id, visible=True).all()
    socials = Social.objects.filter(user_id=user_id).all()
    social_data = {
        i: parse_socials(j)
        for i, j in groupby(socials, lambda social: social.section_id.section_id)
    }
    user_data = CustomUser.objects.get(id=user_id)
    histories = History.objects.filter(user_id=user_id, visible=True).all()
    histories_data = {
        i: categorize_histories(j)
        for i, j in groupby(histories, lambda history: history.section_id.section_id)
    }

    context = {
        "sections": sections,
        "histories": histories_data,
        "socials": social_data,
        "user": user_data,
        "form": MessageForm(),
        "message": message
    }

    return render(request, "cms_core/index.html", context)
