from django.shortcuts import render
import json

def index(request):

    with open("../data/Jane_Addams.json", "r", encoding="utf-8") as f:
        json_arquivo = json.load(f)

    context = {
            "arquivo":"Isto é uma variável",
            "json": json_arquivo
        }

    return render(request, "index.html", context=context)