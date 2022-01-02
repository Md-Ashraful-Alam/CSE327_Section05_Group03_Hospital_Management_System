from django.contrib import admin

from .models import BloodDonate
from .models import Bed



# Register your models here.

admin.site.register(Bed)
admin.site.register(BloodDonate)
