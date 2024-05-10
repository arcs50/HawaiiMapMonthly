from django.urls import path

from . import views

urlpatterns = [
    path("<int:month>/<int:year>", views.home, name="home"),
    path("time_lapse/",views.time_lapse, name="time_lapse")
]