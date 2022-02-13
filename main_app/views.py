from django.views.generic.base import TemplateView # <- a class to handle sending a type of response
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View 
from .models import Card, Print

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
    fields = ['name', 'img', 'price', 'verified_card']
    template_name = "card_create.html"
    def get_success_url(self):
        return reverse('card_detail', kwargs={'pk': self.object.pk})


class CardDetail(DetailView):
    model = Card
    template_name = "card_detail.html"



class CardUpdate(UpdateView):
    model = Card
    fields = ['name', 'img', 'price', 'verified_card']
    template_name = "card_update.html"
    def get_success_url(self):
        return reverse('card_detail', kwargs={'pk': self.object.pk})

class CardDelete(DeleteView):
    model = Card
    template_name = "card_delete_confirmation.html"
    success_url = "/cards/"


class PrintCreate(View):
    
    def post(self, request, pk):
        name= request.POST.get("name")
        img = request.POST.get("img")
        price = request.POST.get("price")
        card = Card.objects.get(pk=pk)
        Print.objects.create(name=name, img = img, price = price, card=card)
        return redirect('artist_detail', pk=pk)


    # <!-- for length {{song.length // 60:song.length%60}}  instead -->



