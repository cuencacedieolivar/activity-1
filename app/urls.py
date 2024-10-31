from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (HomePageView,
    CategoryListView, CategoryDetailView,
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    OrderCreateView, OrderListView, OrderDetailView,
    ReviewCreateView, ReviewListView
)

urlpatterns = [

    # Product URLs
    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/new/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    # Category URLs
    path('', HomePageView.as_view(), name='home'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),

    # Order URLs
    path('orders/new/', OrderCreateView.as_view(), name='order_create'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),

    # Review URLs
    path('products/<int:product_id>/reviews/new/', ReviewCreateView.as_view(), name='review_create'),
    path('products/<int:product_id>/reviews/', ReviewListView.as_view(), name='review_list'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)