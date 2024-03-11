from django.urls import path
from coreapp.views import ProductAPIView

urlpatterns = [
     path('products/', ProductAPIView.as_view(), name='product-order'),
]
