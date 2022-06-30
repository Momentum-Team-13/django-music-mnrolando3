from django.db import models
# from django.core.validators import RegexValidator
# from users.models import User


class Album(models.Model):
    title = models.CharField(maxlength=250, null=True, blank=True)
    artist = models.CharField(maxlength=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True,
                                      blank=True)
