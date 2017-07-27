# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Plan
from ..login_app.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from datetime import datetime
# Create your views here.
def genErrors(request, Emessages):
    for message in Emessages:
        messages.error(request, message)

def index(request):
    #User.objects.all().delete()
    try:
        request.session['user_id']
    except KeyError:
        return redirect("/")
    myplans = Plan.objects.filter(Q(owner = request.session['user_id']) | Q(joiners = request.session['user_id'])).all()
    other = Plan.objects.exclude(Q(owner = request.session['user_id']) | Q(joiners = request.session['user_id'])).all()
    context = {
    'myplans': myplans.order_by("-created_at"),
    'other': other.order_by("-created_at")
    }
    return render(request, 'commerce/index.html', context)

def plandetails(request, plan_id):
    try:
        request.session['user_id']
    except KeyError:
        return redirect("/")
    plan = Plan.objects.get(id = plan_id)
    users = User.objects.filter(joiners = plan_id).all()
    context = {
    'plan': plan,
    "user":users,
    }
    return render(request, 'travelbuddy/plandetails.html', context)

def addtravelplan(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect("/")
    return render(request, 'travelbuddy/addtravelplan.html')

def addtripplan(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect("/")
    print request.POST['travelstartdate']
    print datetime.now().date()
    plan = Plan.objects.createPlan(request.POST, request.session['user_id'])
    if plan['status'] == True:
        messages.success(request, 'Travel Plan Created!')
    else:
        genErrors(request, plan['errors'])
        return redirect("/user/addtravelplan")
    return redirect('/user/home')

def join(request, plan_id):
    try:
        request.session['user_id']
    except KeyError:
        return redirect("/")
    this_user = User.objects.get(id=request.session['user_id'])
    this_plan = Plan.objects.get(id=plan_id)
    this_plan.joiners.add(this_user)
    return redirect("/user/home")
