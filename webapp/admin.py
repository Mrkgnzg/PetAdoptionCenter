from django.contrib import admin
from .models import Animal, Shelter, AdoptionRequest

admin.site.register(Animal)
admin.site.register(Shelter)
admin.site.register(AdoptionRequest)


