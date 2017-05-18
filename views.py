# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def index(request):
  context = {}

  if request.user.is_authenticated:
  	context['username'] = request.user.username
  else:
  	context['username'] = ''
  
  return render(request, 'avatar/index.html', context)
