# Generated by Django 4.1.4 on 2022-12-15 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_system', '0002_remove_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='are_you_doctor',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
