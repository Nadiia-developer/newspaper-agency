# Generated by Django 4.2.7 on 2023-12-05 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0002_newspaper_content_newspaper_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redactor',
            name='years_of_experience',
            field=models.CharField(max_length=255),
        ),
    ]
