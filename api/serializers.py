from rest_framework import serializers


class BlurSerializer(serializers.Serializer):
    raw_image = serializers.ImageField()
    rate = serializers.IntegerField(min_value=1, max_value=100)
