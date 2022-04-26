from attr import field
from django.contrib import admin
from .models import Items
from .models import Comment


# Register your models here.

admin.site.register(Items)

admin.site.register(Comment)

fields = ( 'image_tag', )
readonly_fields = ('image_tag',)


