from sqlite3 import Timestamp
from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from .utils import slugify_instance_title
from django.urls import reverse
from django.db.models import Q
from django.conf import settings

User = settings.AUTH_USER_MODEL

# custorm query set for the model
class ArticleQuerySet(models.QuerySet):
    def search(self, query=None):
            if query is None or query == "":
                return self.none()

            lookups = Q(title__icontains=query) | Q(content__icontains=query)
            return self.filter(lookups)

class  ArticleManager(models.Manager):

    # overring get_queryset method for ArticleQuerySet model
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)

class Article(models.Model):

    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    Timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"slug": self.slug})

    objects = ArticleManager()

def article_pre_save(sender, instance, *args, **kwargs):
    # print("Pre-Save: ")
    # print(args, kwargs)
    # print(sender, instance)
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(article_pre_save, sender=Article)

def article_post_save(sender, instance, created ,*args, **kwargs):
    # print("Post-Save: ")
    # print(args, kwargs)
    if created:
        slugify_instance_title(instance, save=True)

post_save.connect(article_post_save, sender=Article)

