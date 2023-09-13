from django.shortcuts import render

# Create your views here.

# define your home view
def home(request):
    # unlike EJS templating, we need the html file
    # extension
    return render(request , 'home.html')

# define your about view
def about(request):
    # unlike EJS templating, we need the html file
    # extension
    return render(request , 'about.html')





