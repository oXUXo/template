from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.

class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
	STATUS_CHOICES = (
		('draft','Draft'),
		('published', 'Published'),
	)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	cover = models.ImageField(upload_to="blog/", verbose_name="封面", max_length=100, blank=True)
	# author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
	content = RichTextUploadingField()
	description = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
	objects = models.Manager()
	published = PublishedManager()

	def get_absolute_url(self):
		return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title


# class Comment(models.Model):
# 	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
# 	name = models.CharField(max_length=80)
# 	email = models.EmailField()
# 	created = models.DateTimeField(auto_now_add=True)
# 	updated = models.DateTimeField(auto_now=True)
# 	active = models.BooleanField(default=True)
#
# 	class Meta:
# 		ordering = ('created',)
#
# 	def __str__(self):
# 		return 'Comment by {} on {}'.format(self.name, self.post)
