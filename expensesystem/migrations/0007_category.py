# Generated by Django 3.2.12 on 2022-04-06 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensesystem', '0006_rename_us_expense_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Cateory',
            },
        ),
    ]