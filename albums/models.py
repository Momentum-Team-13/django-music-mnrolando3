from django.db import models
# from django.core.validators import RegexValidator
# from users.models import User


# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    artist = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True,
                                      blank=True)
