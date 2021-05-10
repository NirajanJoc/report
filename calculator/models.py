from django.db import models

# Create your models here.
class Weight(models.Model):
    weight_range=models.CharField(max_length=20, unique=True)
    weight_measure=models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.weight_range} / {self.weight_measure}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Height(models.Model):
    height_range=models.CharField(max_length=20, unique=True)
    height_measure=models.CharField(max_length=20, unique=True)

    
    def __str__(self):
        return f"{self.height_range} / {self.height_measure}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
class BmiCalculate(models.Model):
    user=models.CharField(max_length=50,)
    weight=models.ForeignKey(Weight, on_delete=models.CASCADE)
    height=models.ForeignKey(Height, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"