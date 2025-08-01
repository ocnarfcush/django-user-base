from django.conf import settings
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    address = models.CharField(max_length=255, blank=True)
    birthday = models.DateField(null=True, blank=True)
    facebook_url = models.URLField(blank=True)
    # add whatever other “profile” fields you need

    def __str__(self):
        return f"{self.user.username} profile"
