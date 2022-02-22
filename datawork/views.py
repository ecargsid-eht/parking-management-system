from datetime import date, datetime
from django.shortcuts import redirect, render

from datawork.forms import *
from .models import *
from django.db.models import Sum
# Create your views here.

def index(r):
    data = {
        "total_booking":Vehicle.objects.count(),
        "today_booking":Vehicle.objects.filter(vehicle_arrival__date=date.today()).count(),
        "total_earning":Vehicle.objects.aggregate(Sum("vehicle_category__category_price")),
        "today_earning":Vehicle.objects.filter(vehicle_arrival__date=date.today()).aggregate(Sum("vehicle_category__category_price")),
        "category":Category.objects.count()
    }
    return render(r,"index.html",data)

def manageCustomers(r):
    error = ""
    form = VehicleForm(r.POST or None, r.FILES or None)
    data = {
        "error":error,
        "form":form,
        "vehicle":Vehicle.objects.exclude(vehicle_arrival__date=date.today()),
        "today_vehicle":Vehicle.objects.filter(vehicle_arrival__date=date.today())  

    }
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(manageCustomers)
    return render(r,"manageCustomer.html",data)


def departCustomer(r,vehicle_id):
    vehicle = Vehicle.objects.get(pk=vehicle_id)
    if r.method == "GET":
        vehicle.vehicle_departure = datetime.now()
        vehicle.save()
        return redirect(manageCustomers)