# Generated by Django 3.1.3 on 2022-03-29 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20220328_0157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='id',
        ),
        migrations.AlterField(
            model_name='account',
            name='useremail',
            field=models.EmailField(default='', max_length=128, primary_key=True, serialize=False, verbose_name='이메일'),
        ),
    ]
