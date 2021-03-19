from django.db import models
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120, blank=False)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(blank=True, null=False)
    featured = models.BooleanField(default=True) # null=True, default=True

    def get_absolute_url(self):
        return reverse("products1:product-num", kwargs={"my_id": self.id})  #f"/products/{self.id}/"