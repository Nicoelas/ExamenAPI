from django.urls import path
from . import views

urlpatterns = [
    path('socios/', views.SocioList.as_view(), name='socios-list'),
    path('socios/<int:pk>/', views.SocioDetalle.as_view(), name='socio-detalle'),
]
