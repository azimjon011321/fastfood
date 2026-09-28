from django.urls import path

from .views import home, send_order, checkout, success

urlpatterns = [

    path("", home, name="home"),

    path("send-order/", send_order, name="send_order"),

    path("checkout/", checkout, name="checkout"),

    path("success/", success, name="success"),

]