# Generated by Django 5.0.7 on 2024-08-04 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0002_alter_startup_batch_alter_startup_logo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='batch',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='logo',
            field=models.ImageField(upload_to='startup_logos/'),
        ),
        migrations.AlterField(
            model_name='startup',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='startup',
            name='tags',
            field=models.CharField(max_length=200),
        ),
    ]
