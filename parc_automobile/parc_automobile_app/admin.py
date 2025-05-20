from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Vehicule)
admin.site.register(Notification)
admin.site.register(Depense)
admin.site.register(Trajet)
admin.site.register(Maintenance)
