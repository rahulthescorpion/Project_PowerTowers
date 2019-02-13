from django.db import models

# Create your models here.
class QueryForm(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 50)
    mobile = models.IntegerField()
    comments = models.CharField(max_length = 100)

class Meta:
    db_table = "ClientRequest"
