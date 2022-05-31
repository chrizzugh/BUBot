from django.contrib import admin
from .models import parallel_corpus
# Register your models here.

from .models import *

admin.site.register(user_report)
admin.site.register(user_feedback)
admin.site.register(bubotcollection)
admin.site.register(parallel_corpus)
