from django.db import models
from django.utils import timezone

class Micropost(models.Model):
    user_id = models.ForeignKey('auth.User', related_name='microposts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=140)
    published_date = models.DateTimeField(
            blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
