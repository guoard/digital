from django.db import models


class CommonProperty(models.Model):
    brand = models.CharField(max_length=50)
    price = models.PositiveBigIntegerField()
    year = models.CharField(max_length=4)

    class Meta:
        abstract = True


class Mobile(CommonProperty):
    screen = models.CharField(max_length=50)
    cpu = models.CharField(max_length=50)
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE, related_name='mobiles')


class HandsFree(CommonProperty):
    class SoundQuality(models.IntegerChoices):
        BAD = 1, 'Bad'
        MEDIUM = 2, 'Medium'
        GOOD = 3, 'Good'

    Type = models.CharField(max_length=50)
    sound_quality = models.IntegerField(choices=SoundQuality.choices)


class Seller(models.Model):
    name = models.CharField(max_length=50)
    mobile_price = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name
