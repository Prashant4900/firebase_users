from django.db import models
from users.models import FirebaseUsers


# Create your models here.
class DummyModel(models.Model):
    uuid = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=50)
    user = models.ForeignKey(FirebaseUsers, on_delete=models.CASCADE, null=True, blank=True, related_name="realtime_user")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "DummyRT"
