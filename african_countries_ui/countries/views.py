import requests
from requests.exceptions import RequestException
from django.shortcuts import render
from django.http import Http404

API_BASE_URL = "http://127.0.0.1:8000"

# View to get random African countries.
def country_list(request):
    try:
        response = requests.get(f"{API_BASE_URL}/countries", timeout=5)
        response.raise_for_status()  # Raises an error for bad status codes
        countries = response.json()
        return render(request, 'countries/country_list.html', {'countries': countries})
    except (RequestException, ValueError):
        raise Http404("Countries not found or API error")

# View to get a country by its name
def get_country(request, country_name):
    try:
        response = requests.get(f"{API_BASE_URL}/countries/{country_name}", timeout=5)
        response.raise_for_status()
        country = response.json()
        return render(request, 'countries/country_detail.html', {'country': country})
    except (RequestException, ValueError):
        raise Http404(f"Country {country_name} not found or API error.")