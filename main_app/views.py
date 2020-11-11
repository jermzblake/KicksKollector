from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Kick
from .forms import ViewingForm

# class Kick:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, brand, colorway, releasedate):
#     self.name = name
#     self.brand = brand
#     self.colorway = colorway
#     self.releasedate = releasedate


# kicks = [
#   Kick('Nike Air Yeezy 2 Red October', 'Nike', 'Red', '02/09/2014'),
#   Kick('Jordan 3 Retro Black Cat', 'Air Jordan', 'Black/Dark Charcoal-Black', '06/16/2007'),
#   Kick('Reebok Question', 'Reebok', 'White/Red Suede Toe', '1996')
# ]

def home(request):
    return HttpResponse('<h1> Can i Kick it!?</h1>')

def about(request):
    return render(request, 'about.html')

def kicks_index(request):
    kicks = Kick.objects.all()
    return render(request, 'kicks/index.html', { 'kicks': kicks})

def kicks_detail(request, kick_id):
    kick = Kick.objects.get(id=kick_id)
    # instantiate ViewingForm to be rendered in the template
    viewing_form = ViewingForm()
    return render(request, 'kicks/detail.html', {
        #include the kicks and the viewing_form in the context
        'kick': kick, 'viewing_form': viewing_form})

class KickCreate(CreateView):
    model = Kick
    fields = '__all__'

class KickUpdate(UpdateView):
    model = Kick
    fields = ['colorway', 'releasedate']

class KickDelete(DeleteView):
    model = Kick
    success_url = '/kicks/'

