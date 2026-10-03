from rest_framework import serializers
from .models import Conference, WordPart


class WordPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordPart
        fields = '__all__'


class ConferenceSerializer(serializers.ModelSerializer):
    word_parts = WordPartSerializer(many=True, read_only=True)

    class Meta:
        model = Conference
        fields = '__all__'