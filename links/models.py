from django.db import models
from django.contrib.auth import get_user_model
from managers import ActiveLinkManager

# Create your models here.


class Link(models.Model):
    target_url = models.URLField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    identifier = models.SlugField(blank=True, unique=True, max_length=20)
    objects = models.Manager()
    public = ActiveLinkManager()
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField()
    active = models.BooleanField(default=True)
