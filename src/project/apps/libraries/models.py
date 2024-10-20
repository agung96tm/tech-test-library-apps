import uuid

from django.db import models


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    bio = models.TextField()
    birth_date = models.DateField()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    publish_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    class Meta:
        ordering = ("-publish_date", "title")

    def __str__(self):
        return self.title
