from django.shortcuts import render


# Create your views here.
def login_function(request):
    return render(request, 'login_template.html', {})