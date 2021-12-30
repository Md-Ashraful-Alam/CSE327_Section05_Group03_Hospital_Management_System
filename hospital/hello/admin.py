from django.contrib import admin

from .models import Story
from .models import Patient



# Register your models here.

admin.site.register(Story)
admin.site.register(Patient)
