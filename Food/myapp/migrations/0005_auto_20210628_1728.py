# Generated by Django 3.2.4 on 2021-06-28 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_menu_item_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restraunt',
            name='menu',
        ),
        migrations.AddField(
            model_name='restraunt',
            name='menu',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.menu'),
        ),
    ]
