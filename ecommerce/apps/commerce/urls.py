from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^home$', views.index),
    url(r'^account$', views.accountdetails),
    url(r'^addproduct$', views.addproductpage),
    url(r'^verifyproduct$', views.verifyproduct),
    url(r'^product/(?P<product_id>\d+)$', views.productdetails)
]
