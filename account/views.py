from django.shortcuts import render

# Create your views here.
def account_function(request):
    return render(request, 'account_template.html', {})