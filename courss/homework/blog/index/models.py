from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.



class Atik(models.Model):

    tit = models.CharField(max_length=250)
    jounalis = models.CharField(max_length=100)
    kontni = models.TextField(max_length=5000)
    slug = models.SlugField(max_length=150)
    
    dat_pibliye = models.DateField(default=timezone.now)

    def __str__(self):
        return self.tit


 