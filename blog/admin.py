from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Post

# Register your models here.

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)
