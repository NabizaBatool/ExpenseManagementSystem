# Generated by Django 3.2.12 on 2022-04-01 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=42)),
                ('category', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
