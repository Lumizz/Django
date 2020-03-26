#views.py
from django.shortcuts import render
def home(request):
  return render(request,'index.html')

return render(request,'result.html',{'home_input':user_input}) # assign value

#urls.py
from . import views

path('',views.home) # local dir, function home

#settings.py
TEMPLATES = [
  ...
  'DIRS' : ['templates'] # your dir name where stores html files

]

import os.path
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join('static'),)  # indicates the directory for html to src (css,js,img .. etc)

#index.html
{% load static %}
<link rel="stylesheet" href="{% static 'main.css' %}">

<a href="{% url 'about' %}">Go to about page</a>

<script type="text/javascript" src="{% static 'main.js' %}"></script>

<img src="{% static 'elephant.jpg' %}" alt="">

<p>{{home_input}}</p> #Get the post value
