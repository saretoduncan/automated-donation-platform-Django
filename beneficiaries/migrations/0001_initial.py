# Generated by Django 3.2.7 on 2021-10-16 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='beneficiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiary_id', models.IntegerField()),
                ('beneficiaryname', models.CharField(max_length=30)),
                ('beneficiaryaddress', models.CharField(max_length=30)),
                ('phonenumber', models.IntegerField()),
            ],
        ),
    ]
