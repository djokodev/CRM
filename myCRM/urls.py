from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("products.urls")),
    path("customers/", include("customers.urls")),
    path("orders/", include("orders.urls")),
    path("admin/", admin.site.urls),
]
