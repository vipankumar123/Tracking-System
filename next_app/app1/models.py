from django.db import models
from accounts.models import User

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
    user_id = models.ForeignKey("accounts.User", on_delete = models.CASCADE)
    certificate_id = models.ForeignKey(certificate, on_delete = models.CASCADE)
    file_path = models.FileField()
    issue_date = models.DateTimeField(auto_now_add=False)
    expire_date = models.DateTimeField(auto_now_add=False)


class jobtype(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class jobs(models.Model):
    user_id = models.ForeignKey("accounts.User", related_name = 'by', on_delete = models.CASCADE)
    jobtype = models.ForeignKey(jobtype, related_name = 'job_type', on_delete = models.CASCADE)
    name = models.CharField(max_length = 30)
    description = models.TextField(max_length = 500)
    # estimating_completing_hour = models.FloatField()
    is_completed = models.BooleanField(default = True)

    def __str__(self):
        return str(self.id)


class jobassignment(models.Model):
    Status = (
        ('assigned', 'assigned'),
        ('in_progress', 'in_progress'),
        ('unassigned', 'unassigned'),
        ('completed', 'completed')
    )

    user_id = models.ForeignKey("accounts.User", related_name = 'auth', on_delete = models.CASCADE)
    assigned_to = models.ForeignKey("accounts.User", related_name = 'assign', on_delete = models.CASCADE)
    job_id = models.ForeignKey(jobs, related_name = 'job', on_delete = models.CASCADE)
    assign_time = models.DateField(auto_now = True)
    assignment_status = models.CharField(max_length=250, choices=Status, default='assigned')
    completed_time = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return str(self.id)

class notes(models.Model):
    job_assignment_id = models.ForeignKey(jobassignment, on_delete = models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    owner = models.ForeignKey("accounts.User", on_delete = models.CASCADE, null=True, blank=True)
    job = models.ForeignKey(jobs,on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id)





    









