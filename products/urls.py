from django.urls import path
from .views import HomeView, ProductList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete

urlpatterns = [
    # path('', views.home, name="home"),
    path('', ProductList, name="home"),
    path('all-products/', ProductList, name="products"),
    path('product-detail/<int:pk>/', ProductDetail, name="product-detail" ),
    path('product-create/', ProductCreate, name="product-create" ), 
    path('product-update/<int:pk>/', ProductUpdate, name="product-update" ),
    path('product-delete/<int:pk>/', ProductDelete, name="product-delete" ),
    
    
    
]