from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Kick, Lace
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
    # Get the toys the cat doesn't have
    laces_kick_doesnt_have = Lace.objects.exclude(id__in = kick.laces.all().values_list('id'))
    # instantiate ViewingForm to be rendered in the template
    viewing_form = ViewingForm()
    return render(request, 'kicks/detail.html', {
        #include the kicks and the viewing_form in the context
        'kick': kick, 'viewing_form': viewing_form,
        # Add the laces to be displayed
        'laces': laces_kick_doesnt_have
        })

def add_viewing(request, kick_id):
    # create a ModelForm instance using the data in request.POST
    form = ViewingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_viewing = form.save(commit=False)
        new_viewing.kick_id = kick_id
        new_viewing.save()
    return redirect('detail', kick_id=kick_id)


def assoc_lace(request, kick_id, lace_id):
    Kick.objects.get(id=kick_id).laces.add(lace_id)
    return redirect('detail', kick_id=kick_id)

def disassoc_lace(request, kick_id, lace_id):
    Kick.objects.get(id=kick_id).laces.remove(lace_id)
    return redirect('detail', kick_id=kick_id)


class KickCreate(CreateView):
    model = Kick
    fields = '__all__'

class KickUpdate(UpdateView):
    model = Kick
    fields = ['colorway', 'releasedate']

class KickDelete(DeleteView):
    model = Kick
    success_url = '/kicks/'

