from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.views.generic.base import TemplateView # <- a class to handle sending a type of response
from .models import Card
from django.views.generic.edit import CreateView

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class

class Home(TemplateView):
    template_name = "home.html"
   

class CardList(TemplateView):
    template_name = "card_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["cards"] = Card.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["cards"] = Card.objects.all()
            context["header"] = "Trending Cards"
        return context

class CardCreate(CreateView):
    model = Card
    fields = ['name', 'img', 'price', 'verified_artist']
    template_name = "card_create.html"
    success_url = "/cards/"




    # <!-- for length {{song.length // 60:song.length%60}}  instead -->
