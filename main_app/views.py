from django.shortcuts import render

# Create your views here.

# define your home view
def home(request):
    # unlike EJS templating, we need the html file
    # extension
    return render(request , 'home.html')






# Simulated finch data
# finches = [
    # {
    #     'name': 'Zebra Finch',
    #     'color': 'Orange-cheeked',
    #     'size': 'Small',
    #     'habitat': 'Grasslands',
    # },
    # {
    #     'name': 'Gouldian Finch',
    #     'color': 'Multicolored',
    #     'size': 'Small',
    #     'habitat': 'Savannahs',
    # },
    # Add more finch dictionaries as needed
#]

#def index(request):
#   return render(request, 'finches/index.html', {'finches': finches})

#def about(request):
#    return render(request, 'finches/about.html')


