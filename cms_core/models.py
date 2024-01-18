from django.contrib.auth.models import AbstractUser
from django.db import models

from datetime import datetime


def user_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT /images/user_<id>/<filename>
    return 'media/images/user_{0}/{1}'.format(instance.user_id_id, filename)


IMAGE_TYPES_CHOICES = [
    ('i', 'Icon'),
    ('l', 'Large'),
    ('m', 'Medium'),
]


class CustomUser(AbstractUser):
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=11)
    fullname = models.CharField(max_length=128)
    birth_date = models.DateField(default=datetime.now)
    description = models.TextField()
    job = models.CharField(max_length=64)
    website = models.CharField(max_length=64)


class Image(models.Model):
    image_id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to=user_image_directory_path)
    type = models.CharField(max_length=64, choices=IMAGE_TYPES_CHOICES)
    user_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.image.name.split('/')[-1]


SECTION_TYPES_CHOICES = [
    ("h", "Home"),
    ("a", "About"),
    ("r", "Resume"),
    ("p", "Portfolio"),
    ("s", "Services"),
    ("c", "Contact"),
]


class Section(models.Model):
    section_id = models.IntegerField(primary_key=True)
    header = models.CharField(max_length=64)
    description = models.TextField()
    order = models.IntegerField()
    visible = models.BooleanField()
    type = models.CharField(max_length=64, choices=SECTION_TYPES_CHOICES)
    user_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    image_id = models.ForeignKey(  # only large images
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.header

    class Meta:
        ordering = ['order', 'section_id']


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
    user_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name


class Statistic(models.Model):
    statistic_id = models.IntegerField(primary_key=True)
    value = models.FloatField()
    label = models.CharField(max_length=64)
    section_id = models.ForeignKey(
        Section,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    user_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.label


def user_cv_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT /cvs/user_<id>/<filename>
    return 'media/cvs/user_{0}/{1}'.format(instance.user_id_id, filename)


class CV(models.Model):
    cv_id = models.IntegerField(primary_key=True)
    file = models.FileField(upload_to=user_cv_directory_path)
    section_id = models.ForeignKey(
        Section,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    user_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.file.name


HISTORY_TYPES_CHOICES = [
    ('w', "Work"),
    ('e', "Education")
]


class History(models.Model):
    history_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=64)
    description = models.TextField()
    visible = models.BooleanField()
    type = models.CharField(max_length=64, choices=HISTORY_TYPES_CHOICES)
    date_started = models.DateTimeField()
    date_ended = models.DateTimeField(null=True, blank=True)
    section_id = models.ForeignKey(
        Section,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    user_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "histories"


class Service(models.Model):
    service_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64)
    description = models.TextField()
    order = models.IntegerField()
    visible = models.BooleanField()
    image_id = models.ForeignKey(  # only icons
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    section_id = models.ForeignKey(
        Section,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    user_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.title


class Project(models.Model):
    project_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64)
    description = models.TextField()
    tag = models.CharField(max_length=64)
    link = models.CharField(max_length=64)
    visible = models.BooleanField()
    image_id = models.ForeignKey(  # only medium images
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    section_id = models.ForeignKey(
        Section,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    user_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.title


class Social(models.Model):
    social_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64)
    link = models.CharField(max_length=64)
    image_id = models.ForeignKey(  # only icon images
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    section_id = models.ForeignKey(
        Section,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    user_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.title


class Message(models.Model):
    message_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=254)
    subject = models.CharField(max_length=64)
    message = models.TextField()
    user_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.subject
