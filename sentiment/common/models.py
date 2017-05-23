from django.db import models


class Sentiment1Grams(models.Model):
    phrase = models.CharField(max_length=50, primary_key=True)
    rate = models.IntegerField


class Sentiment2Grams(models.Model):
    phrase = models.CharField(max_length=100, primary_key=True)
    rate = models.IntegerField


class Sentiment3Grams(models.Model):
    phrase = models.CharField(max_length=150, primary_key=True)
    rate = models.IntegerField
