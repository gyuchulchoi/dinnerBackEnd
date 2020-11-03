from django.db import models

class Bon(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    type = models.CharField(max_length=50)
    disc = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'bon'