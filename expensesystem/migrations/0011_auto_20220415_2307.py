# Generated by Django 3.2.12 on 2022-04-15 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expensesystem', '0010_auto_20220415_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='avatar-2.jpg', null=True, upload_to='pic/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='userProfile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
