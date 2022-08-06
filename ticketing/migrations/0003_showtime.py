# Generated by Django 4.0.4 on 2022-05-14 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0002_cinema'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('salable_sits', models.IntegerField()),
                ('free_sits', models.IntegerField()),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketing.cinema')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketing.movie')),
            ],
        ),
    ]
