# Generated by Django 3.1 on 2020-08-24 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20200824_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsimage',
            name='news_images',
        ),
        migrations.AddField(
            model_name='newsitem',
            name='news_images',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='news.newsimage'),
        ),
    ]
