from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contacts
from django.core.mail import send_mail
from django.contrib import messages, auth
from django.contrib.auth.models import User


def contact(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        car_name = request.POST['car_name']
        car_manager = request.POST['car_manager']
        car_id = request.POST['car_id']
        name = request.POST['name']        
        phone = request.POST['phone']
        email = request.POST['email']
        manager_email = request.POST['manager_email']
        message = request.POST['text']
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contacts.objects.all().filter(
                car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "This car alredy rented")
                return redirect("/carlist")
        contact = Contacts(car=car_name, car_id=car_id, name=name, email=email,
                           phone=phone, message=message, user_id=user_id, car_manager=car_manager)
        contact.save()
        send_mail(
            'New order',
            'Rent order. '+ name + ' ' + car_name + ' ' + phone+ ' ' + email + ' ' + message, 
            'raisakulakovska1@gmail.com',
            [manager_email],
            fail_silently=False,
        )
        messages.success(request, "Your request submited")
        return redirect('accounts:dashboard')
