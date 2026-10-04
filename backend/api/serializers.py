from rest_framework import serializers
from .models import (
    Conference,
    WordPart,
    Shoba,
    Maqola,
    AboutShoba
)


class WordPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordPart
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutShoba
        fields = '__all__'


class MaqolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maqola
        fields = '__all__'


class ShobaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoba
        fields = '__all__'


class ShobaMalumotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoba
        fields = ['id', 'title', 'slug']


class ConferenceSerializer(serializers.ModelSerializer):
    word_parts = WordPartSerializer(
        many=True,
        read_only=True
    )

    shobalar = ShobaMalumotSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Conference
        fields = '__all__'