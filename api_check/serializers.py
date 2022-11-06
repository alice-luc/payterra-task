from rest_framework import serializers
from api_check.models import BinRecognitionRequest


class BinRecognitionRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = BinRecognitionRequest
        fields = '__all__'

    def check_if_expired(self, bin_number):
        pass