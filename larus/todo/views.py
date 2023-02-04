from django.shortcuts import render
from django.views.generic import TemplateView

class BaseHomePage(TemplateView):
    template_name = 'todo/base.html'
