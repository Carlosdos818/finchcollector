from django.contrib import admin
# Import our finch model
# Register your models here.
from .models import Finch

# Register your models here
admin.site.register(Finch)
