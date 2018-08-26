from django.db import models

class Micropost(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()

    def publish(self):
        self.save()
