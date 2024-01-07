from django.urls import path
from .views import SignUp
from django.contrib.auth import views as authViews

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('logout/', authViews.LogoutView.as_view(), name='logout'),
]