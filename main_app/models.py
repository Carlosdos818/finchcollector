from django.db import models
# need the reverse method from django urls for redirects
from django.urls import reverse
# import date module from datetime
from datetime import date

# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Model for Toys
# Toys will be a M:M with finches
# Finches >---< Toys
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.color} {self.name}'
    
    def get_absolute_url(self):
        return reverse('toy_detail', kwargs={'pk': self.id})

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    habitat = models.CharField(max_length=100)
    toys = models.ManyToManyField(Toy)
    
    def __str__(self):
        return self.name
    
    # this is used to redirects from class based views
    # kwargs are unknown number of arguments
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    

    # add a method to determine finch hunger
    def fed_for_today(self):
        # Filter produces an (QuerySet) for all feedings from current date
        # Count the items in that array, compare to the length of MEALS (tuple)
        # We'll return a boolean that we can use in our template
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
    

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

    

    #  Add Meta class to change the default sorting
    class Meta:
        ordering=['-date']