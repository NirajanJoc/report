from django.db import models

# Create your models here.
class Profile(models.Model):
    CHOICE_GENDER=(
        ('male','MALE'),
        ('female','FEMALE')
    )
    user=models.CharField(max_length=255, null=True, blank=True)
    firstname=models.CharField(max_length=30, null=True, blank=True)
    middlename=models.CharField(max_length=20, null=True, blank=True)
    lastname=models.CharField(max_length=20, null=True, blank=True)
    gender=models.CharField(max_length=20, choices=CHOICE_GENDER, default='male')
    avatar=models.ImageField(upload_to='avatar/', blank=True, null=True)
    contact=models.CharField(max_length=20, null=True, blank=True)
    address=models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)