from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="类目名")
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modified = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    def get_absolute_url(self):
        return reverse('product:product_list_by_category', args=[self.slug])

    class Meta:
        ordering = ("name",)
        verbose_name = "类目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="型号")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="类目")
    oe = models.TextField(default="", verbose_name="OE号")
    keywords = models.CharField(max_length=200, verbose_name="关键词")
    intro = models.CharField(max_length=200, verbose_name="简介")
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, verbose_name="价格")
    image = models.ImageField(upload_to="product/", verbose_name="产品图片", max_length=100, blank=True)
    car = models.CharField(max_length=200, verbose_name="适用车辆")
    net_weight = models.DecimalField(default=0.0, max_digits=20, decimal_places=2, verbose_name="净重")
    gross_weight = models.DecimalField(default=0.0, max_digits=20, decimal_places=2, verbose_name="毛重")
    pcs_carton = models.IntegerField(verbose_name="每箱数量", blank=True, null=True)
    means = models.CharField(max_length=200, default="", verbose_name="长*宽*高", blank=True, null=True)
    active = models.BooleanField(default=True, verbose_name="是否在售")
    stock = models.IntegerField(default=0, verbose_name="库存")
    detail = models.TextField(verbose_name="详细说明", blank=True, null=True)
    amazon = models.URLField(max_length=200, verbose_name="亚马逊链接", blank=True, null=True)
    slug = models.SlugField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modified = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    def get_absolute_url(self):
        return reverse('product:product-detail', args=[self.id, self.slug])

    class Meta:
        verbose_name = "产品"
        verbose_name_plural = verbose_name
        ordering = ("-created",)

    def __str__(self):
        return self.name
