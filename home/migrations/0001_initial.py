# Generated by Django 2.2.5 on 2019-10-05 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.EmailField(max_length=150)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
