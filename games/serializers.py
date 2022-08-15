from rest_framework import serializers
from .models import Game


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "owner", "title", "platform", "created_at", "updated_at")
        model = Game
