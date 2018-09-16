from django.contrib import admin
from . import models
# Register your models here.


def SelectAl(modeladmin, request, queryset):
    obj = models.AlgorithmArticle.objects.filter(Tag='algorithm')
    list_display = (obj, )


SelectAl.short_description = 'Select Algorithm'


class AlgorithmArticleAmdin(admin.ModelAdmin):
    list_display = ('Title', 'Content', 'Time', 'Tag')
    list_editable = ('Content', 'Tag')
    actions = [SelectAl]


admin.site.register(models.AlgorithmArticle, AlgorithmArticleAmdin)
