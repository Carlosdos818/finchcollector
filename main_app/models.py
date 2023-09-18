from django.db import models
# need the reverse method from django urls for redirects
from django.urls import reverse

# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    habitat = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    # this is used to redirects from class based views
    # kwargs are unknown number of arguments
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    

    # Model for Feeding (Finch -|---< Feeding)
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    # creates finch FK reference
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
    

    def __str__(self):
        # Use the 'meal' attribute directly to get the meal name
        return f"{self.get_meal_display()} on {self.date}"
