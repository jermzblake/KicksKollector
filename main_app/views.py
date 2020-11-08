from django.shortcuts import render
from django.http import HttpResponse

class Kick:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, brand, colorway, releasedate):
    self.name = name
    self.brand = brand
    self.colorway = colorway
    self.releasedate = releasedate


kicks = [
  Kick('Nike Air Yeezy 2 Red October', 'Nike', 'Red', '02/09/2014'),
  Kick('Jordan 3 Retro Black Cat', 'Air Jordan', 'Black/Dark Charcoal-Black', '06/16/2007'),
  Kick('Reebok Question', 'Reebok', 'White/Red Suede Toe', '1996')
]

def home(request):
    return HttpResponse('<h1> Can i Kick it!?</h1>')

def about(request):
    return render(request, 'about.html')

def kicks_index(request):

    #get a list of cats and put in a variable called kicks

    return render(request, 'kicks/index.html', { 'kicks': kicks})
