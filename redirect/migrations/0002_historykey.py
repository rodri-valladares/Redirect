# Generated by Django 3.2.8 on 2022-12-30 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redirect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=30)),
                ('query_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('C', 'in cache'), ('D', 'in database'), ('N', 'not exist')], max_length=12)),
            ],
        ),
    ]
