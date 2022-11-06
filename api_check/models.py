from datetime import datetime

from django.db import models


class BinRecognitionRequest(models.Model):

    bin = models.PositiveIntegerField(verbose_name='Bin Number')
    date_created = models.DateTimeField(verbose_name='Date of last request', default=datetime.now())
    bank_name = models.CharField(max_length=250, verbose_name='Bank name')

    class Meta:
        verbose_name = "Known Bin number"
        verbose_name_plural = "Known Bin numbers"

    def __str__(self):
        return self.bank_name

    objects = models.Manager()



