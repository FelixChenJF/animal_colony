from django.db import models
import datetime

class Mice(models.Model):
  clippedDate = models.CharField(max_length=15, null=True) #(("Date"), default=datetime.date.today)
  genotypedOrNot = models.CharField(max_length = 1, null=True)
  genotyper = models.CharField(max_length=3, null=True)
  earmark = models.CharField(max_length=5, null=True)
  sex = models.CharField(max_length=1, null=True)
  box = models.CharField(max_length=5, null=True)
  dob = models.CharField(max_length=15, null=True) #(("Date"), default=datetime.date.today)
  mother = models.CharField(max_length=255, null=True)
  father = models.CharField(max_length=255, null=True)
  strain = models.CharField(max_length=255, null=True)
  cre1 = models.CharField(max_length=3, null=True)
  cre2 = models.CharField(max_length=3, null=True)
  gasp = models.CharField(max_length=3, null=True)
  