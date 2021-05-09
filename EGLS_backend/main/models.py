from django.db import models

# Create your models here.
from django.db import models


class UserFavoritesLinks(models.Model):
    title = models.CharField(max_length=50, primary_key=True, db_index=True)
    pf_index = models.IntegerField()
    rid = models.CharField(max_length=20)
    quality = models.IntegerField()
