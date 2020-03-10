from django.db import models, transaction
from random import randrange

from django.utils.functional import cached_property


class City(models.Model):
    name = models.TextField()
    population = models.BigIntegerField()


class School(models.Model):
    name = models.TextField()
    number = models.SmallIntegerField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    @property
    def total_articles(self):
        articles = 0
        for student in self.student_set.all():
            articles += student.number_of_articles
        return articles

    @cached_property
    def total_articles_cached(self):
        articles = 0
        for student in self.student_set.all():
            articles += student.number_of_articles
        return articles


class Student(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    number_of_classes = models.IntegerField(default=randrange(0,10))
    number_of_articles = models.IntegerField(default=randrange(0, 20))
