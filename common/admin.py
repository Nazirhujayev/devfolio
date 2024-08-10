from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(Intro)
admin.site.register(About)
admin.site.register(Skills)
admin.site.register(Skills_percent)
admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(Thoughts)
admin.site.register(BlogCategory)
admin.site.register(Contact)
admin.site.register(Contact_us)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug":("title",)}

admin.site.register(BlogComment)