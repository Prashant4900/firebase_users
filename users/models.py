from django.db import models
from django.utils.html import mark_safe


# Create your models here
class FirebaseUsers(models.Model):
    uid = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=50, default="Guest User", blank=True)
    email = models.EmailField(max_length=100, default="user@example.com")
    password = models.CharField(max_length=500, blank=True, default="")
    verified = models.BooleanField(default=False, blank=True)
    disabled = models.BooleanField(default=False, blank=True)
    user_image = models.URLField(default="", blank=True)
    create_at = models.DateTimeField()
    last_sign_in = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(blank=True, max_length=20)
    provider = models.CharField(max_length=50, default="Password", blank=True)

    def __str__(self):
        return self.name

    @property
    def image_preview(self):
        if self.user_image:
            return mark_safe('<img src="{}" width="150"/>'.format(self.user_image))
        return ""

    class Meta:
        verbose_name = 'Firebase Users'
        verbose_name_plural = 'Users'
