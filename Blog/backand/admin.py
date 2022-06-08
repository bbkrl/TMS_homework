from django.contrib import admin
from backand import models


admin.site.register(models.User)
admin.site.register(models.Author)
admin.site.register(models.Reader)
admin.site.register(models.Category)
admin.site.register(models.Post)
admin.site.register(models.Comment)
admin.site.register(models.Subscription)




# @admin.register
# class BlogAdmin(admin.ModelAdmin):
#     filter_horizontal = ['category']
