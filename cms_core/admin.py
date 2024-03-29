from typing import Any
from django import forms
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.contrib.auth.models import Group
from .models import Section, Skill, Image, Statistic, CV, History, Service, Project, Social, Message, CustomUser

admin.site.unregister(Group)


class RequestUserModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        query = super().get_queryset(request).filter(user_id=request.user.id)
        return query

    def save_model(self, request, obj, form, change):
        # associating the current logged in user to the client_id
        obj.user_id = request.user
        super().save_model(request, obj, form, change)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    fields = ["fullname", "birth_date", "description", "address", "phone_number", "job", "website", "email"]
    list_display = ["id", "username", "fullname"]

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        query = super().get_queryset(request).filter(id=request.user.id)
        return query

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Image)
class ImageAdmin(RequestUserModelAdmin):
    fields = ["image", "type"]
    list_display = ["image_id", "image", "type", "user_id"]


@admin.register(Section)
class SectionAdmin(RequestUserModelAdmin):
    fields = ["header", "description", "order", "visible", "type", "image_id"]
    list_display = ["section_id", "header", "order", "visible", "type", "user_id", "image_id"]

    def get_form(self, request, obj=None, **kwargs):
        form = super(SectionAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['image_id'].queryset = Image.objects.filter(user_id=request.user).filter(type='l')
        return form


class SkillAdminForm(forms.ModelForm):
    class Meta:
        model = Skill
        widgets = {
            'value': forms.NumberInput(attrs={'min': 0, 'max': 100, 'step': 5}),
        }
        fields = ["name", "value", "visibility", "section_id"]

@admin.register(Skill)
class SkillAdmin(RequestUserModelAdmin):
    fields = ["name", "value", "visibility", "section_id"]
    list_display = ["skill_id", "name", "value", "visibility", "section_id", "user_id"]
    form = SkillAdminForm

    def get_form(self, request, obj=None, **kwargs):
        form = super(SkillAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['section_id'].queryset = Section.objects.filter(user_id=request.user, type='a')
        return form


@admin.register(Statistic)
class StatisticAdmin(RequestUserModelAdmin):
    fields = ["value", "label", "section_id"]
    list_display = ["statistic_id", "value", "label", "section_id", "user_id"]

    def get_form(self, request, obj=None, **kwargs):
        form = super(StatisticAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['section_id'].queryset = Section.objects.filter(user_id=request.user, type='c')
        return form


@admin.register(CV)
class CVAdmin(RequestUserModelAdmin):
    fields = ["file", "section_id"]
    list_display = ["cv_id", "file", "section_id", "user_id"]

    def get_form(self, request, obj=None, **kwargs):
        form = super(CVAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['section_id'].queryset = Section.objects.filter(user_id=request.user, type='a')
        return form


@admin.register(History)
class HistoryAdmin(RequestUserModelAdmin):
    fields = ["title", "subtitle", "description", "visible", "type", "date_started", "date_ended", "section_id"]
    list_display = ["history_id", "title", "subtitle", "visible",
                    "type", "date_started", "date_ended", "section_id", "user_id"]

    def get_form(self, request, obj=None, **kwargs):
        form = super(HistoryAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['section_id'].queryset = Section.objects.filter(user_id=request.user, type='r')
        return form


@admin.register(Service)
class ServiceAdmin(RequestUserModelAdmin):
    fields = ["title", "description", "order", "visible", "image_id", "section_id"]
    list_display = ["service_id", "title", "order", "visible", "image_id", "section_id", "user_id"]

    def get_form(self, request, obj=None, **kwargs):
        form = super(ServiceAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['image_id'].queryset = Image.objects.filter(user_id=request.user).filter(type='i')
        form.base_fields['section_id'].queryset = Section.objects.filter(user_id=request.user, type='s')
        return form


@admin.register(Project)
class ProjectAdmin(RequestUserModelAdmin):
    fields = ["title", "description", "tag", "link", "visible", "image_id", "section_id"]
    list_display = ["project_id", "title", "tag", "link", "visible", "image_id", "section_id", "user_id"]

    def get_form(self, request, obj=None, **kwargs):
        form = super(ProjectAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['image_id'].queryset = Image.objects.filter(user_id=request.user).filter(type='m')
        form.base_fields['section_id'].queryset = Section.objects.filter(user_id=request.user, type='p')
        return form


@admin.register(Social)
class SocialAdmin(RequestUserModelAdmin):
    fields = ["title", "link", "image_id", "section_id"]
    list_display = ["social_id", "title", "link", "image_id", "section_id", "user_id"]

    def get_form(self, request, obj=None, **kwargs):
        form = super(SocialAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['image_id'].queryset = Image.objects.filter(user_id=request.user).filter(type='i')
        form.base_fields['section_id'].queryset = Section.objects.filter(user_id=request.user, type='h')
        return form


@admin.register(Message)
class MessageAdmin(RequestUserModelAdmin):
    fields = ["name", "email", "subject", "message"]
    list_display = ["message_id", "name", "email", "subject", "message", "user_id"]

    def has_add_permission(self, request, obj=None):
        return False
