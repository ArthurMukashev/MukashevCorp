from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import InformationSchema, AccessMatrix


# Register your models here.

admin.site.register(InformationSchema, SimpleHistoryAdmin)
admin.site.register(AccessMatrix)
