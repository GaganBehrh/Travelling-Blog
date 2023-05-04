# Generated by Django 4.1.3 on 2023-02-23 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsblog', '0002_tripcalculator_alter_post_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='TripCalculator',
        ),
    ]