from django.db import models

class Journal(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title