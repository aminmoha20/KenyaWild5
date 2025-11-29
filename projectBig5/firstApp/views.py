from django.shortcuts import render
from django.http import HttpResponse

def homePage(request):
    return render(request,"main.html")

def search(request):
    query = request.GET.get('q', '').lower()
    animals = {
        "lion": "images/lion.jpg",
        "leopard": "images/leopard.jpg",
        "elephant": "images/elephant.jpg",
        "rhino": "images/rhino.jpg",
        "buffalo": "images/buffalo.jpg",
    }
    result = animals.get(query)
    return render(request, "search.html", {"query": query, "result": result})