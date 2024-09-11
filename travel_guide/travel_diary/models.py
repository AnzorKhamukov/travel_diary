from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class TravelEntry(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    heritage_sites = models.TextField()
    places_to_visit = models.TextField()
    rating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))

    def __str__(self):
        return self.location

    @property
    def get_cost_display(self):
        return f"${self.cost}"

    @property
    def heritage_sites_list(self):
        return self.heritage_sites.split(',')

    @property
    def places_to_visit_list(self):
        return self.places_to_visit.split(',')
