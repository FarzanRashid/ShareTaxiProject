# Generated by Django 4.1.7 on 2023-04-06 05:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nav_app', '0003_rename_getuserinfo_riderequest_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='riderequest',
            old_name='location',
            new_name='destination_location',
        ),
        migrations.AddField(
            model_name='riderequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='riderequest',
            name='pickup_location',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='riderequest',
            name='email',
            field=models.EmailField(default='notprovided@empty.com', max_length=254),
            preserve_default=False,
        ),
    ]