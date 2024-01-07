from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import SignUpForm

from django.contrib.auth.decorators import login_required


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'


@login_required
class LogOutView(TemplateView):
    template_name = "registration/logout.html"

