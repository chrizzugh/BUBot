from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(user_report)
admin.site.register(user_feedback)
admin.site.register(bubotcollection)
