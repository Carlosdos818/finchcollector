from django.contrib import admin
# Import our finch model
# Register your models here.
from .models import Finch, Feeding, Toy

# Register your models here
admin.site.register(Finch)
admin.site.register(Feeding)
admin.site.register(Toy)
