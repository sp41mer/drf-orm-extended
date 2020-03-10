import django
from django.db.models import F

django.setup()

from lecture_orm_extended.models import Student, City, School
from random import randrange


def populate_db():

    cities = [City.objects.create(name="City {}".format(i * 42), population=randrange(100000, 200000)) for i in range(0,10)]
    schools = [School.objects.create(name="School of {}".format(city.name), number=randrange(9999), city=city) for i in range(0,10) for city in cities]
    student = [Student.objects.create(name="Student #{}".format(randrange(9999)), age=randrange(9,17), school=school) for i in range(0,10) for school in schools]


def update_city_population():

    city = City.objects.first()
    city.population += 1
    city.save()


def update_city_population_extended():
    city = City.objects.first()
    city.population = F('population') + 1
    city.save()


# populate_db()
update_city_population()
update_city_population_extended()
