import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'
django.setup()

from django.db.models import F
from lecture_orm_extended.models import Student, City, School


def update_city_population():

    city = City.objects.first()
    print('Population', city.population)
    city.population += 1
    city.save()
    print('Population', city.population)


def update_city_population_extended():
    city = City.objects.first()
    print('Extended population', city.population)
    city.population = F('population') + 1
    city.save()
    print('Extended population', city.population)


def update_city_population_extended_refresh():
    city = City.objects.first()
    print('Refresh Extended population', city.population)
    city.population = F('population') + 1
    city.save()
    print('Refresh Extended population', city.population)
    city.refresh_from_db()
    print('Refresh Extended population', city.population)


def double_update_city_population_extended():
    city = City.objects.first()
    print('Double update population', city.population)
    city.population = F('population') + 1
    city.save()
    city.name = "Updated"
    city.save()
    city.refresh_from_db()
    print('Double update population', city.population)


def correct_double_update_city_population_extended():
    city = City.objects.first()
    print('Double update population', city.population)
    city.population = F('population') + 1
    city.save()
    city.refresh_from_db()
    city.name = "Updated"
    city.save()
    city.refresh_from_db()
    print('Double update population', city.population)


update_city_population()
update_city_population_extended()
update_city_population_extended_refresh()
correct_double_update_city_population_extended()
