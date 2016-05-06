from __future__ import unicode_literals

from django.db import models

class Comment(models.Model):
    text = models.TextField(default="")
    author = models.TextField(default="")
