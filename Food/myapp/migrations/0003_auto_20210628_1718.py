# Generated by Django 3.2.4 on 2021-06-28 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_menu_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restraunt',
            name='menu',
        ),
        migrations.AddField(
            model_name='restraunt',
            name='menu',
            field=models.ManyToManyField(to='myapp.Menu'),
        ),
    ]
