from django.contrib import admin
from . import models

# Register your models here.
# 注册后即可在admin里管理


class RequestAdmin(admin.ModelAdmin):
    list_display = ('Username', 'Target', 'Issucceed', 'Date')
    list_filter = ('Date', )    # 过滤器
    list_editable = ('Target', 'Issucceed')


admin.site.register(models.Request, RequestAdmin)


class PageStructureAdmin(admin.ModelAdmin):
    list_display = ('Pagename', 'Link', 'Img', 'Content', 'Trycount')
    list_editable = ('Link', 'Img', 'Content', 'Trycount')


admin.site.register(models.PageStructrue, PageStructureAdmin)


class XinLangAdmin(admin.ModelAdmin):
    list_display = ('Keyword', 'Link', 'SearchHeat', 'Content', 'ScrapyDate')
    list_editable = ('Link', 'SearchHeat', 'Content')


admin.site.register(models.XinLang, XinLangAdmin)


class BaiDuAdmin(admin.ModelAdmin):
    list_display = ('Keyword', 'Link', 'SearchHeat', 'Content', 'ScrapyDate')
    list_editable = ('Link', 'SearchHeat', 'Content')


admin.site.register(models.BaiDu, BaiDuAdmin)


class DouBanAdmin(admin.ModelAdmin):
    list_display = ('Filmname', 'Link', 'Content', 'ScrapyDate')
    list_editable = ('Link', 'Content')


admin.site.register(models.DouBan, DouBanAdmin)


class TengXunAdmin(admin.ModelAdmin):
    list_display = ('Item', 'Link', 'Content', 'ScrapyDate')
    list_editable = ('Link', 'Content')


admin.site.register(models.TengXun, TengXunAdmin)


class GitHubAdmin(admin.ModelAdmin):
    list_display = ('Item', 'Link', 'Content', 'ScrapyDate')
    list_editable = ('Link', 'Content')


admin.site.register(models.GitHub, GitHubAdmin)


class StackOverflowAdmin(admin.ModelAdmin):
    list_display = ('TopQuestion', 'Link', 'Answers', 'Content', 'ScrapyDate')
    list_editable = ('Link', 'Answers', 'Content')


admin.site.register(models.StackOverflow, StackOverflowAdmin)


class ZhiHuAdmin(admin.ModelAdmin):
    list_display = ('Item', 'Link', 'Answers', 'Content', 'ScrapyDate')
    list_editable = ('Link', 'Answers', 'Content')


admin.site.register(models.ZhiHu, ZhiHuAdmin)


class SDUAdmin(admin.ModelAdmin):
    list_display = ('StudentID', 'Password', 'Content', 'ScrapyDate')
    list_editable = ('Password', 'Content')


admin.site.register(models.SDU, SDUAdmin)


class ZhiWangAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Author', 'Insititute', 'Journal', 'Keyword', 'Content', 'ScrapyDate')
    list_editable = ('Author', 'Insititute', 'Journal', 'Keyword', 'Content')


admin.site.register(models.ZhiWang, ZhiWangAdmin)


class SegmentFaultAdmin(admin.ModelAdmin):
    list_display = ('Item', 'Link', 'Author', 'AuthorLink', 'Tag', 'Content', 'ScrapyDate')
    list_editable = ('Link', 'Author', 'AuthorLink', 'Tag', 'Content')


admin.site.register(models.SegmentFault, SegmentFaultAdmin)


class QiDianBookListAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Author', 'Link', 'Description')
    list_editable = ('Author', 'Link', 'Description')


admin.site.register(models.QiDianBookList, QiDianBookListAdmin)


class segmentfaultfullAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_url', 'createdDate', 'tags', 'author', 'author_link')
    list_editable = ('title_url', 'createdDate', 'tags', 'author', 'author_link')


admin.site.register(models.segmentfaultfull, segmentfaultfullAdmin)
