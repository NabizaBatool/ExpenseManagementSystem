# Generated by Django 3.2.12 on 2022-04-06 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expensesystem', '0004_auto_20220406_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='us',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Travel', 'Travel'), ('Clothing', 'Clothing'), ('Groceries', 'Groceries'), ('Accessories', 'Accessories')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]