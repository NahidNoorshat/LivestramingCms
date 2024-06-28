# Generated by Django 5.0 on 2024-06-27 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apihandle", "0002_match_away_team_id_match_fixture_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="league",
            name="country",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="league",
            name="logo",
            field=models.URLField(default="default_logo_url"),
        ),
    ]
