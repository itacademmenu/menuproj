from django.shortcuts import render
from django.views import generic


class AdminView(generic.TemplateView):
    template_name = 'administration/administration.html'




