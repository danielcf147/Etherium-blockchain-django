from django.urls import path
from .views import SmartContractView

urlpatterns = [
    path("smart-contract/", SmartContractView.as_view()),
]
