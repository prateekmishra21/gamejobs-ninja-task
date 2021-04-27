# Generated by Django 3.1.1 on 2021-04-23 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookstore', '0002_auto_20210423_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbook',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userbook',
            name='type',
            field=models.CharField(choices=[['Physical', 'Physical'], ['Ebook', 'Ebook']], max_length=100, null=True),
        ),
    ]