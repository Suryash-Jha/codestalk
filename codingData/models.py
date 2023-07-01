from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class userDetails(models.Model):
    id = models.AutoField(primary_key=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, null=False)
    codestalk_handle = models.CharField(max_length=100, null=False, unique=True)
    country = CountryField()
    university = models.CharField(max_length=100)
    id_codeforces = models.CharField(max_length=100)
    id_codechef = models.CharField(max_length=100)
    id_leetcode = models.CharField(max_length=100)
    id_gfg = models.CharField(max_length=100)
    id_hackkerank = models.CharField(max_length=100)
    totalQuestions_codeforces = models.IntegerField(default=0)
    totalQuestions_codechef = models.IntegerField(default=0)
    totalQuestions_leetcode = models.IntegerField(default=0)
    totalQuestions_gfg = models.IntegerField(default=0)
    totalQuestions_hackkerank = models.IntegerField(default=0)

    def __str__(self):
        return self.codestalk_handle
