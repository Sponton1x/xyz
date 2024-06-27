from django.contrib.auth.models import User
from django.db import models

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    show_link = models.BooleanField(default=True)
    link = models.URLField(blank=True)
    technology = models.ManyToManyField(Technology)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=500, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    show_link = models.BooleanField(default=True)
    link = models.URLField(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Certificates(models.Model):
    name = models.CharField(max_length=50, unique=True)
    organisation = models.CharField(max_length=100)
    photo = models.ImageField(blank=True, null=True, upload_to='certificates/')

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.CharField(max_length=50, unique=True)
    pdf = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.name
