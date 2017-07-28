from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^home$', views.index),
    url(r'^account$', views.accountdetails),
    url(r'^addproduct$', views.addproductpage),
    url(r'^verifyproduct$', views.verifyproduct),
    url(r'^cart$', views.cart),
    url(r'^product/(?P<product_id>\d+)$', views.productdetails),
    url(r'^product/delete/(?P<product_id>\d+)$', views.deleteproduct),
    url(r'^product/addcart/(?P<product_id>\d+)$', views.addcart),
    url(r'^flush$', views.flush),
]
