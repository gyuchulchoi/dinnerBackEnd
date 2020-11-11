from django.db import models

class Bon_Menu(models.Model):
    menu_price = models.IntegerField()
    menu_name = models.CharField(max_length=200)
    menu_new = models.BooleanField()
    menu_best = models.BooleanField()
    menu_type = models.CharField(max_length=200)
    id = models.IntegerField(primary_key= True)
    class Meta:
        managed = False
        db_table = 'bon_menu'