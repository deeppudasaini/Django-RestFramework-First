from django.db import models

# Create your models here.
class Announcement(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=254)
    announcedDate=models.DateField()
    reminderDate=models.DateField()
    status=models.BooleanField(default=False,blank=True,null=True)
    def __str__(self):
        return self.title