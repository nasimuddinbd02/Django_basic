from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('brand/', views.BrandList.as_view(), name='brand'), 
    path('brand/<int:pk>', views.BrandDetail.as_view(), name='brandDetail'),
    path('category/', views.CategoryList.as_view(), name='category'),
    path('category/<int:pk>', views.CategoryDetail.as_view(), name='categorydetail'),
    path('product/', views.ProductList.as_view(), name='product'),
    path('product/<int:pk>', views.ProductDetail.as_view(), name='productDetail')

]