from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kargs):
    return render(request,"home.html",{})

def contact_view(request,*args, **kargs):
    my_context={
        "my_text": "Este es el valor de la clave My_text",
        "my_number": 1234,
        "my_list": [14,'abc', 125, 'retiro']
    }
    return render(request, "contact.html", my_context)

