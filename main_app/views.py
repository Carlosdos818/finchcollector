from django.shortcuts import render, redirect
# We need to import our class based views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# in order to use the model, we have to import
from .models import Finch, Toy
from .forms import FeedingForm

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
    # This will instantiate a feeding form to be rendered in the template
    feeding_form = FeedingForm()
    # Id-List
    id_list = finch.toys.all().values_list('id')
    # print(f'The id_list for the finch toys: {id_list}')
    # print(f'the toys finch dont got: {toys_finch_doesnt_have}')
    # Finch Doesn't have toys
    toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)
    return render(request, 'finches/detail.html', { 'finch': finch, 'feeding_form': feeding_form, 'toys': toys_finch_doesnt_have })

# View for adding a feeding to a finch
def add_feeding(request, finch_id):
    # Create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # We need to make sure the form data is valid
    if form.is_valid():
        # Then we need to add/save the feeding
        # We don't want to save the feeding until the finch is associated
        new_feeding = form.save(commit=False)
        # Associate the feeding with a finch
        new_feeding.finch_id = finch_id
        # Save the feeding
        new_feeding.save()
    # Finally, redirect back to the detail page(which refreshes the info)
    return redirect('detail', finch_id=finch_id)

# Now we can inherit from the CreateView to make our finches create view
class FinchCreate(CreateView):
    model = Finch
    # fields = '__all__'
    # we can also do this if you  only want to pass a few field's items
    fields = ['name', 'color', 'size', 'habitat']

# UpdateView very similar to CreateView, need model and fields
class FinchUpdate(UpdateView):
    model = Finch
    # Lets make it so you can't rename a finch
    fields = ['color', 'size', 'habitat']
# DeleteView very similar to CreateView, need model and fields
class FinchDelete(DeleteView):
    model = Finch
    # Instead of fields or using the absolute_url, we just use a success_url
    success_url = '/finches'


# views for Toys
# ToyList
class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'
# ToyDetail
class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'
# ToyCreate
class ToyCreate(CreateView):
    model = Toy
    fields = ['name', 'color']

    def form_valid(self, form):
        return super().form_valid(form)
# ToyUpdate
class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']
# ToyDelete
class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

# Adds toy to finch
def assoc_toy(request, finch_id, toy_id):
    # To make the association, we target the finch and pass the toy id
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect('detail', finch_id=finch_id)
# Removes toy from finch
def unassoc_toy(request, finch_id, toy_id):
    # To make the association, we target the finch and pass the toy id
    Finch.objects.get(id=finch_id).toys.remove(toy_id)
    return redirect('detail', finch_id=finch_id)
