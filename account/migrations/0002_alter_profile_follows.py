# Generated by Django 3.2.9 on 2021-11-24 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(blank=True, default=None, related_name='followed_by', to='account.Profile'),
        ),
    ]
