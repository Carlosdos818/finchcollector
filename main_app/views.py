from django.shortcuts import render

# Dummy Data.
finches = [
    {
        'name': 'Zebra Finch',
        'color': 'Orange-cheeked',
        'size': 'Small',
        'habitat': 'Grasslands',
    },
    {
        'name': 'Gouldian Finch',
        'color': 'Multicolored',
        'size': 'Small',
        'habitat': 'Savannahs',
    },
    # Add more finch dictionaries as needed
]

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

# Index view for all finches
def finches_index(request):
    # we can pass data to templates, just like we did in express.
    return render(request, 'finches/index.html', {'finches': finches })





