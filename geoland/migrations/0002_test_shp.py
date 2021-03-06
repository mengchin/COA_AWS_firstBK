# Generated by Django 3.2.4 on 2021-06-30 08:49

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    dependencies = [
        ('geoland', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='test_shp',
            fields=[
                ('name', models.TextField(primary_key=sqlalchemy.sql.expression.true, serialize=False)),
                ('hhi', models.TextField(blank=sqlalchemy.sql.expression.true)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(geography=True, srid=4326)),
            ],
            options={
                'ordering': ['name', 'hhi'],
            },
        ),
    ]
