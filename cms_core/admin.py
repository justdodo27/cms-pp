from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Section, Skill, Image, Statistic, CV, History, Service, Project, Social, Message


class UserQuerySet(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        query = super().get_queryset(request).filter(user_id=request.user.id)
        return query

@admin.register(Image)
class ImageAdmin(UserQuerySet):
    fields = ["image", "type", "user_id"]
    list_display = ["image_id", "image", "type", "user_id"]

@admin.register(Section)
class SectionAdmin(UserQuerySet):
    fields = ["header", "description", "order", "visible", "type", "user_id", "image_id"]
    list_display = ["section_id", "header", "description", "order", "visible", "type", "user_id", "image_id"]

@admin.register(Skill)
class SkillAdmin(UserQuerySet):
    fields = ["name", "value", "visibility", "section_id", "user_id"]
    list_display = ["skill_id", "name", "value", "visibility", "section_id", "user_id"]

@admin.register(Statistic)
class StatisticAdmin(UserQuerySet):
    fields = ["value", "label", "section_id", "user_id"]
    list_display = ["statistic_id", "value", "label", "section_id", "user_id"]

@admin.register(CV)
class CVAdmin(UserQuerySet):
    fields = ["file", "section_id", "user_id"]
    list_display = ["cv_id", "file", "section_id", "user_id"]

@admin.register(History)
class HistoryAdmin(UserQuerySet):
    fields = ["title", "subtitle", "description", "visible", "type", "date_started", "date_ended", "section_id", "user_id"]
    list_display = ["history_id", "title", "subtitle", "description", "visible", "type", "date_started", "date_ended", "section_id", "user_id"]

@admin.register(Service)
class ServiceAdmin(UserQuerySet):
    fields = ["title", "description", "order", "visible", "image_id", "section_id", "user_id"]
    list_display = ["service_id", "title", "description", "order", "visible", "image_id", "section_id", "user_id"]

@admin.register(Project)
class ProjectAdmin(UserQuerySet):
    fields = ["title", "description", "tag", "link", "visible", "image_id", "section_id", "user_id"]
    list_display = ["project_id", "title", "description", "tag", "link", "visible", "image_id", "section_id", "user_id"]

@admin.register(Social)
class SocialAdmin(UserQuerySet):
    fields = ["title", "link", "image_id", "section_id", "user_id"]
    list_display = ["social_id", "title", "link", "image_id", "section_id", "user_id"]

@admin.register(Message)
class MessageAdmin(UserQuerySet):
    fields = ["name", "email", "subject", "message", "user_id"]
    list_display = ["message_id", "name", "email", "subject", "message", "user_id"]