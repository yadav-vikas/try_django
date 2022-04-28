from email import contentmanager
from django.test import TestCase
from django.utils.text import slugify
from .models import Article
from .utils import slugify_instance_title

class ArticleTestCase(TestCase):

    def  setUp(self):
        self.number_of_articles = 5
        for i in range(0,self.number_of_articles):
            Article.objects.create(title="hellow world", content="hellow world content")

    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(), self.number_of_articles)

    def test_hellow_world_unique_slug(self):
        obj = Article.objects.all().order_by("id").first()
        title = obj.title
        slug = obj.slug
        slugified_title = slugify(title)
        self.assertEqual(slug,slugified_title)

    def test_hellow_world_slug(self):
        qs = Article.objects.exclude(slug__iexact = 'hellow-world')
        for obj in qs:
            title = obj.title
            slug = obj.slug
            slugified_title = slugify(title)
            self.assertNotEqual(slug,slugified_title)
            
    def test_slugify_instance_title(self):
        obj = Article.objects.all().last()
        new_slugs = []
        for i in range(0,5):
            instance = slugify_instance_title(obj,save=False)
            new_slugs.append(instance.slug)
        unique_slugs = list(set(new_slugs))
        self.assertEqual(len(new_slugs), len(unique_slugs))

    def test_article_search_manager(self):
        qs = Article.objects.search(query = 'hello world')
        self.assertEqual(qs.count(), self.number_of_articles)
        qs = Article.objects.search(query = 'something else')
        self.assertEqual(qs.count(), self.number_of_articles)