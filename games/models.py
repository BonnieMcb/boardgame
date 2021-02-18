from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True, default=None)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Mechanic(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True, default=None)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category_id = models.ManyToManyField(
        Category, related_name='product_category_id', blank=True)
    mechanic_id = models.ManyToManyField(
        Mechanic, related_name='product_mechanic_id', blank=True)
    names = models.CharField(max_length=254)
    min_players = models.IntegerField(null=True, blank=True)
    max_players = models.IntegerField(null=True, blank=True)
    avg_time = models.IntegerField(null=True, blank=True)
    min_time = models.IntegerField(null=True, blank=True)
    max_time = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image_url = models.URLField(max_length=500, blank=True, default=None)
    rank = models.IntegerField(null=True, blank=True)
    bgg_url = models.URLField(max_length=500, blank=True, default=None)
    game_id = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    avg_rating = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=2)
    geek_rating = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)
    num_votes = models.IntegerField(null=True, blank=True)
    owned = models.IntegerField(null=True, blank=True)
    designer = models.CharField(max_length=254, blank=True, default=None)
    weight = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)

    # to make the membership invisible in the shop page
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.names
