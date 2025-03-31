from django.urls import path

from apps.transactions.api.v1.views import AverageOrderView, TransactionView

urlpatterns = [
    path("add_transaction/", TransactionView.as_view()),
    path("average_order_value/", AverageOrderView.as_view()),
]
