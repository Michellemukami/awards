from django.contrib import admin
from .models import Project,Profile
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
   

    admin.site.register(Project)
    admin.site.register(Profile)
