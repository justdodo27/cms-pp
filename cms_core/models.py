from django.contrib.auth.models import User
from django.db import models


SECTION_TYPES_CHOICES = [
    ("a", "about"),
    ("SO", "Sophomore"),
    ("JR", "Junior"),
    ("SR", "Senior"),
    ("GR", "Graduate"),
]

class Section(models.Model):
    section_id = models.IntegerField(primary_key=True)
    header = models.CharField(max_length=64)
    description = models.TextField()
    order = models.IntegerField()
    visible = models.BooleanField()
    type = models.CharField(max_length=64, choices=SECTION_TYPES_CHOICES)
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

class Skill(models.Model):
    skill_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    value = models.FloatField()
    visibility = models.BooleanField()
    section_id = models.ForeignKey(
        Section,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )