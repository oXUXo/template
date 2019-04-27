from django.db import models

# Create your models here.

class Message(models.Model):
    contact = models.CharField(max_length=100, verbose_name="联系人")
    email = models.EmailField(max_length=150, verbose_name="邮箱")
    message = models.TextField(default="", verbose_name="留言")
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modified = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    def __str__(self):
        return self.email
