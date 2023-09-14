from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeTemplateView, contacts, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>', ProductListView.as_view(), name='product'),
]
