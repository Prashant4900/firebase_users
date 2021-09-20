from django.db import models
from users.models import FirebaseUsers


# Create your models here.
class DummyModel(models.Model):
    uid = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=50)
    user1 = models.ForeignKey(FirebaseUsers, null=True, blank=True, on_delete=models.CASCADE,
                              related_name="firestore_user")
    # user = models.ForeignKey(FirebaseUsers, on_delete=models.CharField)
    update_at = models.DateTimeField(blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Dummy"
