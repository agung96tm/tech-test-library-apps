from apps.libraries.models import Author, Book
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            "id",
            "name",
            "bio",
            "birth_date",
        )


class BookSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "description",
            "publish_date",
            "author_id",
        )

    def create(self, validated_data):
        author = validated_data.pop("author_id")
        validated_data["author"] = author
        return super().create(validated_data)

    def update(self, instance, validated_data):
        author = validated_data.pop("author_id")
        if author is not None:
            instance.author = author
        return super().update(instance, validated_data)
