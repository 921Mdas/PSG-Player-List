# Generated by Django 4.0.4 on 2022-04-24 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uworldapp', '0003_alter_performance_options_alter_player_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='score',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='scoring', to='uworldapp.performance'),
        ),
    ]
