# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Product, Review
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
    # myplans = Plan.objects.filter(Q(owner = request.session['user_id']) | Q(joiners = request.session['user_id'])).all()
    # other = Plan.objects.exclude(Q(owner = request.session['user_id']) | Q(joiners = request.session['user_id'])).all()
    products = Product.objects.all()[:8]
    context = {
    # 'myplans': myplans.order_by("-created_at"),
    # 'other': other.order_by("-created_at")
    'products': products
    }
    return render(request, 'commerce/index.html', context)
def productdetails(request, product_id):
    try:
        request.session['user_id']
    except KeyError:
        return redirect("/")
    product = Product.objects.get(id = product_id)
    print product.image_link
    product.views +=1
    product.save()
    #users = User.objects.filter(joiners = plan_id).all()
    context = {
    'product': product,
    #"user":users,
    }
    return render(request, 'commerce/productdetails.html', context)

def accountdetails(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect("/")
    user = User.objects.get(id = request.session['user_id'])
    context = {
    'user': user,
    }
    return render(request, 'commerce/accountdetails.html', context)

def addproductpage(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect("/")
    return render(request, 'commerce/addproduct.html')

def verifyproduct(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect("/")
    product = Product.objects.createProduct(request.POST, request.session['user_id'])
    if product['status'] == True:
        messages.success(request, 'Product Created!')
    else:
        genErrors(request, product['errors'])
        return redirect("/user/addproduct")
    return redirect('/user/home')

def join(request, plan_id):
    try:
        request.session['user_id']
    except KeyError:
        return redirect("/")
    # this_user = User.objects.get(id=request.session['user_id'])
    # this_plan = Plan.objects.get(id=plan_id)
    # this_plan.joiners.add(this_user)
    return redirect("/user/home")

def flush(request):
    #User.objects.all().delete()
    Product.objects.all().delete()
    return redirect('/')
