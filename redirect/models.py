from django.db import models
from django.core import cache


class HistoryKey(models.Model):

    class StateChoice:

        CACHED= "C"
        NO_CACHED= "D"
        NO_EXIST= "N"
        IN_CACHE = (CACHED,"in cache")
        IN_DATABASE = (NO_CACHED,"in database")
        NOT_IN = (NO_EXIST,"not exist")

        CHOICES = [IN_CACHE,IN_DATABASE,NOT_IN]

    key = models.CharField(max_length=30)
    query_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=12,choices=StateChoice.CHOICES)

    @classmethod
    def create_key(cls, key):
        return cls.objects.get(key=key)


class Redirect(models.Model):
    key = models.CharField(max_length=30)
    url = models.CharField(max_length=120)
    active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get_redirect(cls, key):
        try:
            return cls.get_cache_redirect(key)
        except:
            return cls.get_old_redirect(key)

    @classmethod
    def get_old_redirect(cls,key):
        return cls.objects.get(key=key).url
    
    @classmethod
    def get_cache_redirect(cls,key):
        return cache.get(key).url

    class Meta:
        verbose_name = 'Redirect'
        verbose_name_plural = 'Redirects'
        ordering = ['-created_at']