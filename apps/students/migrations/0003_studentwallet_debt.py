# Generated by Django 4.1.3 on 2022-11-25 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0002_alter_studentwallet_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="studentwallet",
            name="debt",
            field=models.FloatField(default=0.0),
        ),
    ]
