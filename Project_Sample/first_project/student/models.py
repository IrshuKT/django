from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    guardian_name = models.CharField(max_length=100)
    address = models.TextField()    
    contact_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='student_photos/')
    
    def __str__(self):
        return self.name