# Generated by Django 4.0.4 on 2022-04-24 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uworldapp', '0002_alter_performance_options_player_score'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='performance',
            options={},
        ),
        migrations.AlterModelOptions(
            name='player',
            options={},
        ),
        migrations.AlterField(
            model_name='player',
            name='score',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='score', to='uworldapp.performance'),
        ),
    ]
