# Generated by Django 2.1.7 on 2020-03-09 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture_orm_extended', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='number_of_articles',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='student',
            name='number_of_classes',
            field=models.IntegerField(default=9),
        ),
    ]
