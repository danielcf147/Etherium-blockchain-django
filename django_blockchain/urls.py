from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("send_transaction.urls")),
    path("api/", include("smart_contract.urls")),
]
