from django.shortcuts import render
# We need to import our class based views
from django.views.generic.edit import CreateView

# in order to use the model, we have to import
from .models import Finch

# This are the old cats, now we user models.
# Dummy Data.
# finches = [
#     {
#         'name': 'Zebra Finch',
#         'color': 'Orange-cheeked',
#         'size': 'Small',
#         'habitat': 'Grasslands',
#     },
#     {
#         'name': 'Gouldian Finch',
#         'color': 'Multicolored',
#         'size': 'Small',
#         'habitat': 'Savannahs',
#     },
   
# ]

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
    # return render(request, 'finches/index.html', {'finches': finches })
    # we need to retrieve our list of finches
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches })


# Details view for a single finch
def finches_detail(request, finch_id):
    # find the finch
    finch = Finch.objects.get(id=finch_id)
    # to check this view function before we have html, use a print
    # print('this is the finch django found')
    # print(finch)
    return render(request, 'finches/detail.html', { 'finch': finch })

# Now we can inherit from the CreateView to make our finches create view
class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    # we can also do this if you  only want to pass a few field's items
    # fields = ['name', 'color', 'size', 'habitat']
    
