from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Section, Skill, Image, Statistic, CV, History, Service, Project, Social, Message


class RequestUserModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        query = super().get_queryset(request).filter(user_id=request.user.id)
        return query
    
    def save_model(self, request, obj, form, change):
        # associating the current logged in user to the client_id
        obj.user_id = request.user
        super().save_model(request, obj, form, change)

@admin.register(Image)
class ImageAdmin(RequestUserModelAdmin):
    fields = ["image", "type"]
    list_display = ["image_id", "image", "type", "user_id"]

@admin.register(Section)
class SectionAdmin(RequestUserModelAdmin):
    fields = ["header", "description", "order", "visible", "type", "image_id"]
    list_display = ["section_id", "header", "description", "order", "visible", "type", "user_id", "image_id"]

@admin.register(Skill)
class SkillAdmin(RequestUserModelAdmin):
    fields = ["name", "value", "visibility", "section_id"]
    list_display = ["skill_id", "name", "value", "visibility", "section_id", "user_id"]

@admin.register(Statistic)
class StatisticAdmin(RequestUserModelAdmin):
    fields = ["value", "label", "section_id"]
    list_display = ["statistic_id", "value", "label", "section_id", "user_id"]

@admin.register(CV)
class CVAdmin(RequestUserModelAdmin):
    fields = ["file", "section_id"]
    list_display = ["cv_id", "file", "section_id", "user_id"]

@admin.register(History)
class HistoryAdmin(RequestUserModelAdmin):
    fields = ["title", "subtitle", "description", "visible", "type", "date_started", "date_ended", "section_id"]
    list_display = ["history_id", "title", "subtitle", "description", "visible", "type", "date_started", "date_ended", "section_id", "user_id"]

@admin.register(Service)
class ServiceAdmin(RequestUserModelAdmin):
    fields = ["title", "description", "order", "visible", "image_id", "section_id"]
    list_display = ["service_id", "title", "description", "order", "visible", "image_id", "section_id", "user_id"]

@admin.register(Project)
class ProjectAdmin(RequestUserModelAdmin):
    fields = ["title", "description", "tag", "link", "visible", "image_id", "section_id"]
    list_display = ["project_id", "title", "description", "tag", "link", "visible", "image_id", "section_id", "user_id"]

@admin.register(Social)
class SocialAdmin(RequestUserModelAdmin):
    fields = ["title", "link", "image_id", "section_id"]
    list_display = ["social_id", "title", "link", "image_id", "section_id", "user_id"]

@admin.register(Message)
class MessageAdmin(RequestUserModelAdmin):
    fields = ["name", "email", "subject", "message"]
    list_display = ["message_id", "name", "email", "subject", "message", "user_id"]