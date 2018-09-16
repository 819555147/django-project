from django.db import models

# Create your models here.
'''一个model表现为一个类，对应数据库中的一张表（ORM）'''


# 请求表
class Request(models.Model):
    Username = models.CharField(max_length=24)
    Target = models.CharField(max_length=20)
    Issucceed = models.BooleanField()
    Date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("Username", "Date"),)

    # 此方法用于改变admin中的显示
    def __str__(self):
        return self.Username


# 目标网页结构表
class PageStructrue(models.Model):
    Pagename = models.CharField(max_length=40)
    Link = models.CharField(max_length=400)
    Img = models.CharField(max_length=400)
    Content = models.CharField(max_length=200)
    Trycount = models.IntegerField(default=0)

    def __str__(self):
        return self.Pagename


# 新浪
class XinLang(models.Model):
    Keyword = models.CharField(max_length=60)
    Link = models.CharField(max_length=300)
    SearchHeat = models.IntegerField()
    Content = models.TextField()
    ScrapyDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("Keyword", "ScrapyDate"),)

    def __str__(self):
        return self.Keyword


# 百度
class BaiDu(models.Model):
    Keyword = models.CharField(max_length=60)
    Link = models.CharField(max_length=300)
    SearchHeat = models.IntegerField()
    Content = models.TextField()
    ScrapyDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("Keyword", "ScrapyDate"),)

    def __str__(self):
        return self.Keyword


# 豆瓣
class DouBan(models.Model):
    Filmname = models.CharField(max_length=60)
    Link = models.CharField(max_length=300)
    Content = models.TextField()
    ScrapyDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("Filmname", "ScrapyDate"),)

    def __str__(self):
        return self.Filmname


# 腾讯
class TengXun(models.Model):
    Item = models.CharField(max_length=60)
    Link = models.CharField(max_length=300)
    Content = models.TextField()
    ScrapyDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("Item", "ScrapyDate"),)

    def __str__(self):
        return self.Item


# GitHub
class GitHub(models.Model):
    Item = models.CharField(max_length=30)
    Link = models.CharField(max_length=300)
    Content = models.TextField()
    ScrapyDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("Item", "ScrapyDate"),)

    def __str__(self):
        return self.Item


# StackOverflow
class StackOverflow(models.Model):
    TopQuestion = models.CharField(max_length=30)
    Link = models.CharField(max_length=300)
    Answers = models.IntegerField()
    Content = models.TextField()
    ScrapyDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("TopQuestion", "ScrapyDate"),)

    def __str__(self):
        return self.TopQuestion


# SegmentFault
class SegmentFault(models.Model):
    Item = models.CharField(max_length=100)
    Link = models.CharField(max_length=300)
    Author = models.CharField(max_length=50)
    AuthorLink = models.CharField(max_length=300)
    Tag = models.CharField(max_length=100)
    Content = models.TextField()
    ScrapyDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("Item", "ScrapyDate"),)

    def __str__(self):
        return self.Item


# 知乎
class ZhiHu(models.Model):
    Item = models.CharField(max_length=60)
    Link = models.CharField(max_length=300)
    Answers = models.IntegerField()
    Content = models.TextField()
    ScrapyDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("Item", "ScrapyDate"),)

    def __str__(self):
        return self.Item


# 校园信息门户网
class SDU(models.Model):
    StudentID = models.DecimalField(max_digits=12, decimal_places=0)
    Password = models.CharField(max_length=16)
    Content = models.TextField()
    ScrapyDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("StudentID", "ScrapyDate"),)

    def __str__(self):
        return self.StudentID


# 知网
class ZhiWang(models.Model):
    Title = models.CharField(max_length=60)
    Author = models.CharField(max_length=20)
    Insititute = models.CharField(max_length=20)
    Journal = models.CharField(max_length=20)
    Keyword = models.CharField(max_length=20)
    Content = models.TextField()
    ScrapyDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("Title", "ScrapyDate"),)

    def __str__(self):
        return self.Title


# 起点中文网
class QiDianBookList(models.Model):
    Title = models.CharField(max_length=20, primary_key=True)
    Author = models.CharField(max_length=15)
    Link = models.URLField()  # verify_exists=True
    Description = models.TextField()

    def __str__(self):
        return self.Title


# 思否全站
class segmentfaultfull(models.Model):
    title = models.CharField(max_length=60, primary_key=True)
    title_url = models.URLField()  # verify_exists=True
    createdDate = models.CharField(max_length=20)
    tags = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    author_link = models.CharField(max_length=100)

    def __str__(self):
        return self.Item