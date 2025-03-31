from django.db.models import Avg
from django.utils.dateparse import parse_date
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.transactions.api.v1.serializers import TransactionSerializer
from apps.transactions.models import Transaction


class TransactionView(APIView):
    def post(self, request):
        if not request.data:
            return Response({"error": "data not found!"}, status=204)
        serializer = TransactionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.error, status=400)
        serializer.save()
        return Response("Transaction Completed successfully!", status=201)


class AverageOrderView(APIView):
    def get(self, request):
        date = request.GET.get("date")
        if not date:
            return Response({"error": "Date is required!"}, status=400)
        try:
            date = parse_date(date)
            if not date:
                raise ValueError
        except ValueError:
            return Response({"error": "Invalid Date Format"}, status=400)
        avg_order_value = Transaction.objects.filter(
            created_at__date__lte=date
        ).aggregate(Avg("amount"))["amount__avg"]
        return Response({"average_order_value": avg_order_value or 0})
