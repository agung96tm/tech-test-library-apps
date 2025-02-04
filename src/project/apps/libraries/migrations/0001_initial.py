# Generated by Django 4.2.12 on 2024-10-20 04:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("bio", models.TextField()),
                ("birth_date", models.DateField()),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("publish_date", models.DateField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="books",
                        to="libraries.author",
                    ),
                ),
            ],
            options={
                "ordering": ("-publish_date", "title"),
            },
        ),
    ]
