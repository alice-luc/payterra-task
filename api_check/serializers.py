from rest_framework import serializers
from api_check.models import BinRecognitionRequest


class BinRecognitionRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = BinRecognitionRequest
        fields = '__all__'


class BinByRequestSerializer(serializers.Serializer):

    bin = serializers.IntegerField()
    date_created = serializers.DateTimeField()
    bank_name = serializers.CharField()

    def update(self, instance, validated_data):
        instance.update(validated_data)

    def create(self, validated_data):
        pass
