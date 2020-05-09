from django.db import models

# Create your models here.
class Label(models.Model):
    label_text = models.CharField(max_length=50)

    def __str__(self):
        return self.label_text

class MonthEntry(models.Model):
    entryDate = models.DateField()
    amount = models.FloatField()
    isPositive = models.BooleanField()
    label = models.ForeignKey(Label, on_delete=models.SET(0))

    def __str__(self):
        return self.label.label_text + " "

class NetWorthEntry(models.Model):
    entryDate = models.DateField()
    amount = models.FloatField()
    isPositive = models.BooleanField()
    label = models.ForeignKey(Label, on_delete=models.SET(0))

    def __str__(self):
        return self.label.label_text + " "
