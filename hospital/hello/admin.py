from django.contrib import admin

from .models import Nurse
from .models import Medicine



# Register your models here.

admin.site.register(Medicine)
admin.site.register(Nurse)
