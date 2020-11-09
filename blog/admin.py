from django.contrib import admin
from .models import Blog, Tag, Profile
# Register your models here.


admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Profile)
