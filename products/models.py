from django.db import models

class menuitems(models.models):
    name=models.CharField(max_length=100)
    description = models.textField()
    price = models.DecimalField(max_DIGIT=6, decimal_places=2)

    def __str__(self):
        return self.name