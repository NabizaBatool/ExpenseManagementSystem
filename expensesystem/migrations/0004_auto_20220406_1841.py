# Generated by Django 3.2.12 on 2022-04-06 13:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('expensesystem', '0003_auto_20220402_0338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='userId',
        ),
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.FloatField(max_length=42, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='expense',
            name='description',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
