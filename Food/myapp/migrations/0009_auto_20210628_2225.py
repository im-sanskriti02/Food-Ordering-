# Generated by Django 3.2.4 on 2021-06-28 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20210628_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='branch',
        ),
        migrations.AlterField(
            model_name='restraunt',
            name='branch',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
    ]