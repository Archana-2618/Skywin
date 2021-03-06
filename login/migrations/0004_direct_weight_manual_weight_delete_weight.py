# Generated by Django 4.0.6 on 2022-07-16 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_input_quantity_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direct_Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_dealer_name', models.CharField(max_length=100)),
                ('weight_type', models.CharField(max_length=100)),
                ('net_weight', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=100)),
                ('total_amount', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manual_Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_dealer_name', models.CharField(max_length=100)),
                ('weight_type', models.CharField(max_length=100)),
                ('gross_weight', models.CharField(max_length=100)),
                ('gunny_bag_weight', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=100)),
                ('total_amount', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Weight',
        ),
    ]
