from django.contrib import admin
from .models import Section, Skill, Image, Statistic, CV, History, Service, Project, Social, Message


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ["image", "type", "user_id"]
    list_display = ["image_id", "image", "type", "user_id"]

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    fields = ["header", "description", "order", "visible", "type", "user_id", "image_id"]
    list_display = ["section_id", "header", "description", "order", "visible", "type", "user_id", "image_id"]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    fields = ["name", "value", "visibility", "section_id", "user_id"]
    list_display = ["skill_id", "name", "value", "visibility", "section_id", "user_id"]

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    fields = ["value", "label", "section_id", "user_id"]
    list_display = ["statistic_id", "value", "label", "section_id", "user_id"]

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    fields = ["file", "section_id", "user_id"]
    list_display = ["cv_id", "file", "section_id", "user_id"]

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    fields = ["title", "subtitle", "description", "visible", "type", "date_started", "date_ended", "section_id", "user_id"]
    list_display = ["history_id", "title", "subtitle", "description", "visible", "type", "date_started", "date_ended", "section_id", "user_id"]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    fields = ["title", "description", "order", "visible", "image_id", "section_id", "user_id"]
    list_display = ["service_id", "title", "description", "order", "visible", "image_id", "section_id", "user_id"]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = ["title", "description", "tag", "link", "visible", "image_id", "section_id", "user_id"]
    list_display = ["project_id", "title", "description", "tag", "link", "visible", "image_id", "section_id", "user_id"]

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    fields = ["title", "link", "image_id", "section_id", "user_id"]
    list_display = ["social_id", "title", "link", "image_id", "section_id", "user_id"]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    fields = ["name", "email", "subject", "message", "user_id"]
    list_display = ["message_id", "name", "email", "subject", "message", "user_id"]