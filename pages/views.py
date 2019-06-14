from django.shortcuts import render

from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {})


def directory(request):
    print("DEBUG")
    brothers = User.objects.order_by('last_name')
    print(brothers)
    return render(request, 'pages/directory.html', {'brothers': brothers})


def account(request):
    return render(request, 'pages/account.html', {})