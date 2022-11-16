from django.urls import path, include
from api_check.views import  BinNumberViewSet

urlpatterns = [
    path('get-bank/', BinNumberViewSet.as_view({
        'get': 'retrieve',
        'post': 'create',
        'put': 'update'
    })),
    # path('api/', include('api_check.urls'))
]
