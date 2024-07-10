# exchange/models.py

from django.db import models

class Brokerage(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Broker(models.Model):
    name = models.CharField(max_length=100)
    brokerage = models.ForeignKey(Brokerage, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Commodity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Contract(models.Model):
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    date = models.DateField()
    type = models.CharField(max_length=10, choices=[('buy', 'Buy'), ('sell', 'Sell')])
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.broker} - {self.commodity} ({self.type})'
