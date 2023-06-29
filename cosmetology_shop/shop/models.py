from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)

    class Meta:
        index_together = (('id','slug'))

    def __str__(self):
        return self.name