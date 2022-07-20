from django.shortcuts import render


def index(request):
    return render(request, "index.html", {"movies": [
        { "name": "فیلم دانیال" },
        { "name": "کارتون دانیال" },
        { "name": "تست تستی" }
    ]})
