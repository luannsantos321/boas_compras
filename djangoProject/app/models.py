from django.db import models

# Create your models here.
class Produto(models.Model):
    produto = models.CharField(max_length=100, verbose_name='Produto')

    class Meta:
        db_table = 'produto'

    def __str__(self):
       return self.produto