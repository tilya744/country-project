from django.shortcuts import render
from countries.models import Country


def get_countries(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        return render(request, 'countries/index.html', {'countries': countries})


def get_country(request, id):
    if request.method == 'GET':
        country = Country.objects.get(id=id)
        return render(request, 'countries/detail.html', {'country': country})