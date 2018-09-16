from django.db import models


# Create your models here.
class AlgorithmArticle(models.Model):
    Title = models.CharField(max_length=40, primary_key=True)
    Content = models.TextField()
    Time = models.DateTimeField(auto_now_add=True)
    Tag = models.CharField(max_length=20)

    def __str__(self):
        return self.Title
