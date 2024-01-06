# Generated by Django 4.2.8 on 2024-01-06 16:13

import cms_core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image_id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to=cms_core.models.user_image_directory_path)),
                ('type', models.CharField(choices=[('i', 'Icon'), ('l', 'Large'), ('m', 'Medium')], max_length=64)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('section_id', models.IntegerField(primary_key=True, serialize=False)),
                ('header', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('order', models.IntegerField()),
                ('visible', models.BooleanField()),
                ('type', models.CharField(choices=[('h', 'Home'), ('a', 'About'), ('r', 'Resume'), ('p', 'Portfolio'), ('s', 'Services'), ('c', 'Contact')], max_length=64)),
                ('image_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_core.image')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('statistic_id', models.IntegerField(primary_key=True, serialize=False)),
                ('value', models.FloatField()),
                ('label', models.CharField(max_length=64)),
                ('section_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_core.section')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('social_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('link', models.CharField(max_length=64)),
                ('image_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_core.image')),
                ('section_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_core.section')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('skill_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('value', models.FloatField()),
                ('visibility', models.BooleanField()),
                ('section_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_core.section')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('order', models.IntegerField()),
                ('visible', models.BooleanField()),
                ('image_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_core.image')),
                ('section_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_core.section')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('tag', models.CharField(max_length=64)),
                ('link', models.CharField(max_length=64)),
                ('visible', models.BooleanField()),
                ('image_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_core.image')),
                ('section_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_core.section')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=254)),
                ('subject', models.CharField(max_length=64)),
                ('message', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('history_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('subtitle', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('visible', models.BooleanField()),
                ('type', models.CharField(choices=[('w', 'Work'), ('e', 'Education')], max_length=64)),
                ('date_started', models.DateTimeField()),
                ('date_ended', models.DateTimeField(null=True)),
                ('section_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_core.section')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CV',
            fields=[
                ('cv_id', models.IntegerField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to=cms_core.models.user_cv_directory_path)),
                ('section_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_core.section')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
