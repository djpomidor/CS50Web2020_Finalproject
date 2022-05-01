from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("user-cabinet", views.user_cabinet_view, name="user-cabinet"),
    path("backside", views.backside, name="backside"),
    path("create-order", views.create_order, name="create-order"),

    path("orders/<int:order_number>", views.orders_view, name="orders-view"),
]
