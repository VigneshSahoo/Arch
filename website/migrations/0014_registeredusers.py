# Generated by Django 4.2.6 on 2023-11-24 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_subscription_alter_services_s_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
