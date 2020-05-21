from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from .models import CarsList
from carmanager.models import CarManager


def index_carlist(request):
    carlist = CarsList.objects.all().filter(is_published=True)

    paginator = Paginator(carlist, 6)
    page = request.GET.get("page")
    paged_carlist = paginator.get_page(page)

    context = {
        "carlist": paged_carlist,
        "title": "Car Rent"
    }

    return render(request, "carlist/carlist.html", context)


def singlecar(request, carlist_id):
    car = get_object_or_404(CarsList, pk=carlist_id)
    singlemanager = get_object_or_404(CarManager, name=car.carmanager)
    context = {
        "car": car,
        'title': "Your Car",
        "singlemanager": singlemanager
    }
    return render(request, "carlist/singlecar.html", context)




