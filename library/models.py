from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.DateField(null=True)
    website = models.URLField(null=True)
    is_deleted = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10),], null=True)


