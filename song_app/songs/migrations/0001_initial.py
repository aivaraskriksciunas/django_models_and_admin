# Generated by Django 4.2.1 on 2023-05-19 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("authors", "0002_alter_author_birth_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Song",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=80)),
                ("duration", models.IntegerField()),
                ("genre", models.CharField(max_length=10)),
                ("release_date", models.DateField(help_text="Song release date")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="authors.author"
                    ),
                ),
            ],
        ),
    ]
