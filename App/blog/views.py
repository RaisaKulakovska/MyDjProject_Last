from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from cars.models import CarsList
from .models import Blog
from contacts.models import Contacts
from carmanager.models import CarManager
from django.contrib import messages, auth
from django.contrib.auth.models import User


def blog(request):
    # blog_list = carlist
    blog_list = CarsList.objects.all()   
    order = Contacts.objects.distinct("car_id")

    blog_list_new = Blog.objects.all()
    order_all = Contacts.objects.all()
    manager_all = CarManager.objects.all() 
    
    context = {
        "order": order,
        "blog_list": blog_list,
        "blog_list_new": blog_list_new,
        'order_all':order_all,
        'manager_all':manager_all,
        "title": "Blog-articles",
        "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit."
    }    
    return render(request, 'blog/blog.html', context)

def comment(request):   

    return render(request, 'blog/comment.html')


def single(request):
    # blog_car = 
    # blog_manager = get_object_or_404(CarManager, name=blog_car.carmanager)

    if request.method == "POST":
        user_id = request.POST['user_id']
        car_id = request.POST['car_id']
        comment = request.POST['comment']
        First_name = request.POST['First_name']
        Last_name = request.POST['Last_name']
  
    context = {        
        'user_id': user_id,
        'car_id': car_id,
        'comment': comment,
        'First_name':First_name,
        'Last_name':Last_name
    }
    
    return render(request, 'blog/single.html', context)

