
from django.urls import path
from .views import *


urlpatterns = [
    path("",index,name="index"),
    path("manage-customers/",manageCustomers,name="manageCustomers"),
    path("<int:vehicle_id>/manage-customers/",departCustomer,name="departCustomer"),
]
