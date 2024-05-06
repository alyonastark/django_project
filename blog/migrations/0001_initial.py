# Generated by Django 5.0.4 on 2024-05-06 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=200, verbose_name="заголовок")),
                (
                    "slug",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="slug"
                    ),
                ),
                ("body", models.TextField(verbose_name="содержимое")),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="blog/", verbose_name="превью"
                    ),
                ),
                ("created_at", models.DateTimeField(verbose_name="дата создания")),
                (
                    "is_published",
                    models.BooleanField(
                        default=True, verbose_name="признак публикации"
                    ),
                ),
                (
                    "view_count",
                    models.IntegerField(
                        default=0, verbose_name="количество просмотров"
                    ),
                ),
            ],
            options={
                "verbose_name": "блоговая запись",
                "verbose_name_plural": "блоговые записи",
            },
        ),
    ]