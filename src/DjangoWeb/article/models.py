from django.db import models
from django.contrib.auth.models import User

class ArticleColumn(models.Model):
    user = models.ForeignKey(User, related_name='Article_column', on_delete=models.CASCADE)
    column = models.CharField(max_length=64)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column
