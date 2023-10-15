from django.urls import path
from . import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView
 
 
urlpatterns = [
    path("Rooms", chat_views.rooms, name="Rooms"),
    path("Room/<str:slug>", chat_views.room, name="Room"),
    # login-section
    path("auth/login/", LoginView.as_view
         (template_name="chat/LoginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]