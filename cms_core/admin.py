from django.contrib import admin
from .models import Section, Skill


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    fields = ["header", "description", "order", "visible", "type", "user_id"]
    list_display = ["header", "description", "order", "visible", "type", "user_id"]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass

