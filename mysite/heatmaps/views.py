from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request, month, year):
    next_month = (month + 1) % 13
    next_year = year
    if next_month == 0:
        next_month = 1
        next_year = (year + 1) % 2024
        if next_year == 0:
            next_year = 2000
    prev_month = month - 1
    prev_year = year
    if prev_month <= 0:
        prev_month = 12
        prev_year = year - 1
        if prev_year <= 1999:
            prev_year = 2023
    filepath = "heatmap" + str(month) + str(year) +".html"
    next_filepath = "heatmap" + str(next_month) + str(next_year) + ".html"
    context = {
        'filepath':filepath,
        'next_filepath': next_filepath,
        'next_month':next_month,
        'next_year':next_year,
        'month':month,
        'year':year,
        'prev_month': prev_month,
        'prev_year': prev_year
    }
    return render(request, 'home.html', context)

def time_lapse(request):
    return render(request, 'time_lapse.html',{})