from django.urls import path
from . import views

app_name = 'WebWithLogin'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:Item_id>/", views.detail, name="detail"),
]