# Generated by Django 2.2.6 on 2020-06-14 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0009_friend'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='friend',
            options={'verbose_name': 'Друг', 'verbose_name_plural': 'Друзья'},
        ),
    ]
