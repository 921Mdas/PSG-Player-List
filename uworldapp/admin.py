from django.contrib import admin

# Register your models here.
from .models import Performance, Player,Photo
admin.site.register(Player)
admin.site.register(Performance)
admin.site.register(Photo)