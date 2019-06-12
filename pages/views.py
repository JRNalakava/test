from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {})


def directory(request):
    return render(request, 'pages/directory.html', {})


def account(request):
    return render(request, 'pages/account.html', {})
