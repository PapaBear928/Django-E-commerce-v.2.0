from django.db import models
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
	""" Creating models to making a category to our blog posts """
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"


class Post(models.Model):
	""" Creating models to making a post in our blog """

	class NewManager(models.Manager):
		def get_queryset(self):
			return super().get_queryset().filter(status='published')

	options = (
		('draft', 'Draft'),
		('published', 'Published')
	)

	category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
	title = models.CharField(max_length=255)
	excerpt = models.TextField(null=True)
	image = models.ImageField(upload_to='blog_posts/', default='blog_posts/default.jpg')
	slug = models.SlugField(max_length=255, unique_for_date='publish')
	publish = models.DateTimeField(default=timezone.now)
	content = models.TextField()
	status = models.CharField(max_length=10, choices=options, default='draft')
	objects = models.Manager()  # default Django menager
	custom = NewManager()  # our custom manago

	def get_absolute_url(self):
		return reverse('blog:read_post', args=[self.slug])

	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title


class Comment(models.Model):
	""" Creating models to making commentary at blog """

	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
	name = models.CharField(max_length=50)
	email = models.EmailField()
	content = models.TextField()
	publish = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=True)

	class Meta:
		ordering = ("-publish",)

	def __str__(self):
		return f"Comment by {self.name}"
