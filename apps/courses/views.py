# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Course
from django.contrib import messages


from django.shortcuts import render,redirect, HttpResponse

def index(request):
    context = {
        'show': Course.objects.all()
    }
    return render(request,"courses/index.html",context)

def add(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        course = Course.objects.create(name = request.POST['name'], desc = request.POST['desc'])
        course.save()
    return redirect("/show")

def show(request):
    context = {
        'show': Course.objects.all()
    }
    return render(request,"courses/index.html",context)

def remove(request,id):
    c = Course.objects.get(id = id)
    context = {
        'show': c
    }
    return render(request,"courses/remove.html",context)

def delete(request,id):
    c = Course.objects.get(id = id)
    c.delete()
    return redirect('/')
    
