# from django.shortcuts import render
from rest_framework import viewsets
import datetime

from rest_framework.response import Response

from api_check.serializers import BinRecognitionRequestSerializer
from api_check.models import BinRecognitionRequest
from api_check.services import send_request_to_binlist


class BinNumberViewSet(viewsets.ModelViewSet):

    serializer_class = BinRecognitionRequestSerializer
    queryset = BinRecognitionRequest.objects.all()

    def get_or_create(self, card_number) -> object:

        instance = self.get_object()
        date_of_last_request = instance.date_created
        allowed_request_date = datetime.datetime.now() - datetime.timedelta(days=7)
        if date_of_last_request < allowed_request_date:
            request = send_request_to_binlist(card_number)
            serializer = self.get_serializer(
                instance,
                bank_name=request.bank_name,
                date_created=request.date_created,
                partial=True
            )
            instance = self.perform_update(serializer)

        return instance

    def retrieve(self, request, *args, **kwargs):

        card_number = request.data.get('card_number')
        instance = self.get_or_create(card_number)
        serializer = self.get_serializer(instance)

        return Response(serializer.data)


