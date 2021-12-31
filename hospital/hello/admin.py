from django.contrib import admin

from .models import User
from .models import OrganDonate



# Register your models here.

admin.site.register(OrganDonate)
admin.site.register(User)