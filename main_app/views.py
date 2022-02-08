from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.views.generic.base import TemplateView # <- a class to handle sending a type of response


# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

class CardList(TemplateView):
    template_name = "card_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cards"] = cards # this is where we add the key into our context object for the view to use
        return context
