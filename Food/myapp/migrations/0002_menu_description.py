# Generated by Django 3.2.4 on 2021-06-28 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]