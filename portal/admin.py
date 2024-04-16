from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Building)
admin.site.register(Material)
admin.site.register(BuildingSystems)
admin.site.register(WallAssembly)
admin.site.register(RoofAssembly)
admin.site.register(FloorAssembly)
admin.site.register(WindowAssembly)
admin.site.register(StructuralAssembly)