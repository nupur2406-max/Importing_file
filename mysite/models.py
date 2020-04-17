
from django.db import models

# Create your models here.
class Data(models.Model):
    id = models.IntegerField(primary_key=True)
    message=models.CharField(max_length=2000)
    truth=models.CharField(max_length=50)
    cube=models.CharField(max_length=50)
    google=models.CharField(max_length=50)
    google_spam=models.FloatField()
    google_not_spam=models.FloatField()
    ibm=models.CharField(max_length=50)
    ibm_spam=models.FloatField()
    ibm_not_spam=models.FloatField()

    def __str__(self):
        return self.message