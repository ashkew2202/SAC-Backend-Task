from django.urls import path
from .views import productCrud, idSpecificProductCrud

urlpatterns = [
    path('', productCrud),
    path('<int:id>', idSpecificProductCrud)
]