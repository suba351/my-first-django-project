from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello world</h1>") # string of HTML
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123
    }
    return render(request, "contact.html", my_context)


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [123, 321, 124, 123, "ABC"]
    }
    return render(request, "about.html", my_context)
