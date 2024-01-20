from typing import Dict

from django.shortcuts import render

from .models import Categorie, Clothe


def portfolio(request):
    clothes_ordered = Clothe.objects.all()

    context: Dict[str, Dict[str, Clothe | Categorie]] = {}
    for clothe in clothes_ordered:
        if clothe.category.name not in context:
            context[clothe.category.name] = {"category": clothe.category, "clothes": []}
        context[clothe.category.name]["clothes"].append(clothe)

    return render(request, "pages/portfolio.html", {"categories": context.values()})
