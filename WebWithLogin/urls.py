from django.urls import path
from . import views

app_name = 'WebWithLogin'
urlpatterns = [
    path("", views.index, name="index"),
    path('subscribe/<int:Item_id>/', views.subscribe_item, name="subscribe_item"),
    path("<int:Item_id>/", views.detail, name="detail"),
    path("profile_page/", views.profile_page, name="profile_page"),
]