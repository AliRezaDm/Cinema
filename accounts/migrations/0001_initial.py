# Generated by Django 4.1 on 2022-08-15 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Prefer not to say'), (4, 'Non-Binary')], verbose_name='Gender')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth date')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('Image', models.ImageField(upload_to='user/profile_Images', verbose_name='Profile Photo')),
                ('balance', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
