# Generated by Django 4.2.7 on 2023-11-09 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clippedDate', models.CharField(max_length=15, null=True)),
                ('genotypedOrNot', models.CharField(max_length=1, null=True)),
                ('genotyper', models.CharField(max_length=3, null=True)),
                ('earmark', models.CharField(max_length=5, null=True)),
                ('sex', models.CharField(max_length=1, null=True)),
                ('box', models.CharField(max_length=5, null=True)),
                ('dob', models.CharField(max_length=15, null=True)),
                ('mother', models.CharField(max_length=255, null=True)),
                ('father', models.CharField(max_length=255, null=True)),
                ('strain', models.CharField(max_length=255, null=True)),
                ('cre1', models.CharField(max_length=3, null=True)),
                ('cre2', models.CharField(max_length=3, null=True)),
                ('gasp', models.CharField(max_length=3, null=True)),
            ],
        ),
    ]
