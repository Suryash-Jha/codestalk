# Generated by Django 4.2.2 on 2023-06-30 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userDetails',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('codestalk_handle', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('id_codeforces', models.CharField(max_length=100)),
                ('id_codechef', models.CharField(max_length=100)),
                ('id_leetcode', models.CharField(max_length=100)),
                ('id_gfg', models.CharField(max_length=100)),
                ('id_hackkerank', models.CharField(max_length=100)),
                ('totalQuestions_codeforces', models.IntegerField()),
                ('totalQuestions_codechef', models.IntegerField()),
                ('totalQuestions_leetcode', models.IntegerField()),
                ('totalQuestions_gfg', models.IntegerField()),
                ('totalQuestions_hackkerank', models.IntegerField()),
            ],
        ),
    ]
