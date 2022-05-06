# Generated by Django 4.0.4 on 2022-05-01 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uworldapp', '0008_player_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uworldapp.player')),
            ],
        ),
    ]
