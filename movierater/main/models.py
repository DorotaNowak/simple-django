from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(default="")
    year = models.IntegerField(null=True, blank=True)
    relased = models.DateField(null=True, blank=True)
    imbd_rating = models.DecimalField(decimal_places=7, max_digits=10, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='plakaty')

    def __str__(self):
        return self.name_with_year()

    def name_with_year(self):
        return str(self.name) + " (" + str(self.year) + ")"
