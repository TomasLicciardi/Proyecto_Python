from django.urls import path
from AppMensajeria.views import *

urlpatterns = [
    path('', MensajeList.as_view(), name="mensajes"),
    path('nuevo/', MensajeCreate.as_view(), name="create_mensajes"),
    path('<pk>/', MensajeDetail.as_view(), name="detail_mensajes"),
    path('eliminar/<pk>', MensajeDelete.as_view(), name="delete_mensajes"),
]