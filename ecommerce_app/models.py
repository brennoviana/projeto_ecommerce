from django.db import models

# Create your models here.

class prod(models.Model):
    
    CATEGORIAS_CHOICES = (
        ("J", "Jogo"),
        ("M", "Mouse"),
        ("T", "Teclado"),
        ("C", "Computadore"),
        ("CON", "Console"),
        ("M", "Monitore"),
        ("P", "Peças"),
    )
    name_prod = models.CharField(max_length=50)
    text_prod = models.TextField(max_length=200)
    price_prod = models.FloatField()
    img_prod = models.ImageField(upload_to='prod/%Y/%m/%d/', default='')
    category = models.CharField(max_length=12, choices=CATEGORIAS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.id} - {self.name_prod}"