from django.shortcuts import render

def index(request):
    remembrancies=["Интервью у памятника","Школьные годы","333","444","555"]
    data = {"header": "Память", "remembrancies": remembrancies}
    return render(request, "firstapp/index.html", context=data)

def fapp_aa(request):
    return render(request, 'firstapp/aa.html', {})

