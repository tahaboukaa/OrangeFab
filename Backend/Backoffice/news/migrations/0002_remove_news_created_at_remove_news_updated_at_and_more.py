# Generated by Django 5.0.7 on 2024-08-04 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='news',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='news',
            name='banner_image',
            field=models.ImageField(upload_to='news_banners/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='place',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='news',
            name='tags',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
