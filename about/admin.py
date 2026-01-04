from django.contrib import admin
from .models import About, Follow


class MyAdmin(admin.ModelAdmin):
     def has_add_permission(self, request, obj=None):
        # count = About.objects.all().count()
        # if count >= 0:
        #     return True
        return False


# Register your models here.
admin.site.register(About, MyAdmin)
admin.site.register(Follow)