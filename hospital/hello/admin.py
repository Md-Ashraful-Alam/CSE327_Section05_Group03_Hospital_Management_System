from django.contrib import admin

from .models import User1
from .models import Bed
from .models import Test
from .models import Appointment


# Register your models here.

admin.site.register(Bed)
admin.site.register(Appointment)
admin.site.register(Test)
admin.site.register(User1)