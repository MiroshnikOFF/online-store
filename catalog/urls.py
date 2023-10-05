from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import HomeTemplateView, contacts, ProductListView, ProductCreateView, ProductUpdateView, \
    ProductDetailView, ProductDeleteView, get_versions_by_product, show_version, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),

    path('contacts/', contacts, name='contacts'),

    path('products/', ProductListView.as_view(), name='products'),
    path('products/create/', never_cache(ProductCreateView.as_view()), name='product_create'),
    path('products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('products/<int:pk>/versions/', get_versions_by_product, name='product_versions'),
    path('products/<int:product_pk>/version/<int:version_pk>/', show_version, name='product_version_detail'),
    path('categories/', CategoryListView.as_view(), name='categories')
]
