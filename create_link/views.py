from django.shortcuts import render
from random import choice
from .models import ShortLink
# Create your views here.


def index(request):
    return render(request=request,template_name='index.html',context={"short_link":"None"})


def create_link(request):
    long_link = request.GET.get("longlink")
    short__link = request.GET.get("short__link")
    
    if short__link is None or short__link == "":
        lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        short__link = ""
        for _ in range(4):
            short__link += choice(lower)
        link = ShortLink.objects.get_or_create(long_link=long_link, short_link=short__link)
    else:
        if len(short__link)>4:
            lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            short__link = ""
            for _ in range(4):
                short__link += choice(lower)
        link = ShortLink.objects.get_or_create(long_link = long_link,short_link = short__link)
    print(link)
    
    return render(request=request,template_name='index.html',context={"short_link": f"http://127.0.0.1:8000/{link[0].short_link}"})