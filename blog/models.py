from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100)
    synopsis = models.CharField(max_length=250)
    date = models.DateField()
    image = models.ImageField(upload_to="blog/images/")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name