from django.forms import ModelForm
from .models import Feeding

# Custom class inheriting from the ModelForm class
# (that gives us all the nice built in methods etc)
class FeedingForm(ModelForm):
    # A nested class Meta - declares the model and fields
    class Meta:
        model = Feeding
        fields = ['date', 'meal']