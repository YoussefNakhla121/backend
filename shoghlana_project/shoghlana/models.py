from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    Name = models.CharField(max_length=100, default='name', null=True)
    type = models.CharField(max_length=50, default='user')
    country = models.CharField(max_length=100, default='country')
    admin_company = models.CharField(max_length=100, default='admin_company', null=True)
    location = models.CharField(max_length=100, default='location', null=True)
    skills = models.CharField(max_length=100, default='skills', null=True)
    occupation = models.CharField(max_length=100, default='occupation', null=True)
    years_of_experience = models.IntegerField(default=0, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="custom_users_set",
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_users_set",
        related_query_name="custom_user",
    )

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Jobs(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()
    job_type = models.CharField(max_length=50)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    def __str__(self):
        return self.title
    
class Application(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    status = models.CharField(max_length=50, default='applied')
    
    def __str__(self):
        return f"{self.user.username} - {self.job.title}"
    
class PostedJobs(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='posted')
    
    def __str__(self):
        return f"{self.user.username} - {self.job.title}"
