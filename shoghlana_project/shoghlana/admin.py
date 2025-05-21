from django.contrib import admin
from .models import Jobs, Users, Application, PostedJobs



# Register your models here.
admin.site.register(Users)
admin.site.register(Jobs)
admin.site.register(Application)
admin.site.register(PostedJobs)