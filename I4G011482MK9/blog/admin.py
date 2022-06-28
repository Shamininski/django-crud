from django.contrib import admin
from .models import PostModel

# Register your models here.
@admin.register(PostModel)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PostModel._meta.get_fields()]
