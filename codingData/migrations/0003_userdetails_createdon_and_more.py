# Generated by Django 4.2.2 on 2023-06-30 16:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('codingData', '0002_alter_userdetails_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='createdOn',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='codestalk_handle',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
