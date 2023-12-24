from django.db import models


class Account(models.Model):

    amount = models.FloatField()
    currency = models.CharField(max_length = 10)

    def __str__(self):
        return f"{self.amount}_{self.currency}"
