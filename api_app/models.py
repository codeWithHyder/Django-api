from django.db import models

class Employees(models.Model):
    
    eno= models.IntegerField()
    edes= models.TextField()
    
    def __str__(self):
        
        return self.edes 
    