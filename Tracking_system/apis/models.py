from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class certificatelevel(models.Model):
    level = models.CharField(max_length=100)

    def __str__(self):
        return self.level


class certificate(models.Model):
    levelofcertificate = models.ForeignKey(certificatelevel, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class usercertificate(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    certificate_id = models.ForeignKey(certificate, on_delete = models.CASCADE)
    file_path = models.FileField()
    issue_date = models.DateTimeField(auto_now_add=False)
    expire_date = models.DateTimeField(auto_now_add=False)