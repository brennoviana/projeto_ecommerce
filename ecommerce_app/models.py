from django.db import models

# Create your models here.

class produto(models.Model):
    nome_prod = models.CharField(max_length=50)
    texto_prod = models.TextField(max_length=200)
    preco_prod = models.FloatField()
    img_prod = models.ImageField(upload_to='media/prod/%Y/%m/%d/', default='produtos/sem_imagem.jpg')
