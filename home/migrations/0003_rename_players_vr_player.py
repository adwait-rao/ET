# Generated by Django 4.2.15 on 2024-08-10 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_players_semester_alter_players_roll_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Players',
            new_name='vr_player',
        ),
    ]
