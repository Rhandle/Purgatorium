from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField
from tinymce.models import HTMLField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager
from django.urls import reverse

User = get_user_model()

# Create your models here.

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=40, blank=True)
    slug = slug = models.SlugField(max_length=40, unique=True, blank=True)
    bio = HTMLField()
    points = models.IntegerField(default=0)
    profile_picture = ResizedImageField(quality=100, upload_to="authors", default="authors/favicon_black.png", null = True, blank = True)

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super(Author, self).save(*args, **kwargs)

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    description = models.TextField(default="No description")

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("post", kwargs={"slug": self.slug})
    
    @property
    def num_posts(self):
        return Post.objects.filter(categories=self).count()
    
    @property
    def last_post(self):
        return Post.objects.filter(categories=self).latest("date")
    
class Comment(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = HTMLField()
    date = models.DateTimeField(auto_now_add=True)
    replies = models.ManyToManyField("Reply", blank=True)

    def __str__(self):
        return self.content[:100]
    
class Reply(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = HTMLField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:100]
    
    class Meta:
        verbose_name_plural = "replies"

class Post(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = HTMLField()
    categories = models.ManyToManyField(Category)
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    tags = TaggableManager()
    comments = models.ManyToManyField(Comment, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
    
    @property
    def num_comments(self):
        return self.comments.count()
    
    @property
    def last_reply(self):
        return self.comments.latest("date")