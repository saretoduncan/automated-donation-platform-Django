# Generated by Django 3.2.7 on 2021-10-16 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='donors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_name', models.CharField(max_length=30)),
                ('email_address', models.CharField(max_length=30)),
                ('phone_number', models.IntegerField()),
                ('image', models.ImageField(default='default.jpeg', upload_to='')),
                ('donor_bio', models.TextField(max_length=255)),
            ],
        ),
    ]
