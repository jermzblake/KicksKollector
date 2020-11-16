from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Kick, Lace
from .forms import ViewingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Import the login_required decorator
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class KickCreate(LoginRequiredMixin, CreateView):
    model = Kick
    fields = ['name', 'brand', 'colorway', 'releasedate']

    # This inherited method is called when a
    # valid kicks form is being submitted
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the kicks
        # Let the CreateView do its job as usual
        return super().form_valid(form)

class KickUpdate(LoginRequiredMixin, UpdateView):
    model = Kick
    fields = ['colorway', 'releasedate']

class KickDelete(LoginRequiredMixin, DeleteView):
    model = Kick
    success_url = '/kicks/'

def home(request):
    return HttpResponse('<h1> Can i Kick it!?</h1>')

def about(request):
    return render(request, 'about.html')

@login_required
def kicks_index(request):
    kicks = Kick.objects.filter(user=request.user)
     # You could also retrieve the logged in user's cats like this
    # kicks = request.user.kick_set.all()
    return render(request, 'kicks/index.html', { 'kicks': kicks})

@login_required
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

@login_required
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

@login_required
def assoc_lace(request, kick_id, lace_id):
    Kick.objects.get(id=kick_id).laces.add(lace_id)
    return redirect('detail', kick_id=kick_id)

@login_required
def disassoc_lace(request, kick_id, lace_id):
    Kick.objects.get(id=kick_id).laces.remove(lace_id)
    return redirect('detail', kick_id=kick_id)




class LaceList(LoginRequiredMixin, ListView):
  model = Lace

class LaceDetail(LoginRequiredMixin, DetailView):
  model = Lace

class LaceCreate(LoginRequiredMixin, CreateView):
  model = Lace
  fields = '__all__'

class LaceUpdate(LoginRequiredMixin, UpdateView):
  model = Lace
  fields = ['name', 'color']

class LaceDelete(LoginRequiredMixin, DeleteView):
  model = Lace
  success_url = '/laces/'
