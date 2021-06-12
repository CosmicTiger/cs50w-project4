from django.db import models
from django.conf import settings
from research.models import Research
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status = 'published')

    STATUS_OPTIONS = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    category = models.ForeignKey(
        Category, on_delete = models.PROTECT, default = 1)
    title = models.CharField(max_length = 250)
    excerpt = models.TextField(null = True)
    content = models.TextField()
    slug = models.SlugField(max_length = 250, unique_for_date = 'published')
    published = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete = models.PROTECT, related_name = 'blog_posts'
    )
    status = models.CharField(
        max_length = 10, choices = STATUS_OPTIONS, default = 'published'
    )
    research_details = models.ManyToManyField(Research, verbose_name="Post Details", related_name="research_to_post")

    objects = models.Manager() # default Manager
    post_objects = PostObjects() # custom Manager

    def __str__(self):
        return self.title
