from django.urls import path

from . import views

app_name = "cms"
urlpatterns = [
    # ex: /cms/
    # path("", views.index, name="index"),
    # ex: /cms/5/
    path("<int:user_id>/", views.website, name="website"),
]