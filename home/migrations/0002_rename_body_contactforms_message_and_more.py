# Generated by Django 4.2.1 on 2023-05-17 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactforms',
            old_name='body',
            new_name='message',
        ),
        migrations.AlterField(
            model_name='contactforms',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]