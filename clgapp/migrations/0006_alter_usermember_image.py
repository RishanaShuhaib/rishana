# Generated by Django 5.0 on 2024-01-05 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clgapp', '0005_remove_usermember_course1_usermember_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermember',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]