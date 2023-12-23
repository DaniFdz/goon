from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        "title": "Portfolio"
    }
    return render(request, 'home.html', context)
