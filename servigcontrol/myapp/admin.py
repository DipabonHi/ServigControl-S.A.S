from django.contrib import admin
from .models import Turno

class TurnoAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha", )
    
# Register your models here.
admin.site.register(Turno, TurnoAdmin)