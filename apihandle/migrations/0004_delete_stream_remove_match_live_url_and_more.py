# Generated by Django 5.0 on 2024-06-27 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apihandle", "0003_league_country_league_logo"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Stream",
        ),
        migrations.RemoveField(
            model_name="match",
            name="live_url",
        ),
        migrations.AddField(
            model_name="match",
            name="away_team_score",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="match",
            name="home_team_score",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="match",
            name="status",
            field=models.CharField(default="Scheduled", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="match",
            name="venue_city",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="match",
            name="venue_name",
            field=models.CharField(default="Unknown", max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="match",
            name="away_team_id",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="match",
            name="fixture_id",
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name="match",
            name="home_team_id",
            field=models.PositiveIntegerField(),
        ),
    ]
