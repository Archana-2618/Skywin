# Generated by Django 4.0.5 on 2022-06-21 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('user_type', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField(unique=True)),
                ('password', models.CharField(max_length=50)),
                ('ifLogged', models.BooleanField(default=False)),
                ('token', models.CharField(default='', max_length=500, null=True)),
            ],
        ),
    ]
