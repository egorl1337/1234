from attr import field
from django.contrib import admin
from .models import Items
from .models import Comment, Comments


# Register your models here.

admin.site.register(Items)

admin.site.register(Comment)

admin.site.register(Comments)


class CommentsAdmin(admin.ModelAdmin):
    exclude = ('user',) # скрыть author поле, чтобы оно не отображалось в форме изменений

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)


fields = ( 'image_tag', )
readonly_fields = ('image_tag',)


