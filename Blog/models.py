from django.db import models

# Create your models here.
class Funcionario(models.Model):
    name=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    
    
    def _str_(self):
        return f"{self.name},{self.title}"
    
    