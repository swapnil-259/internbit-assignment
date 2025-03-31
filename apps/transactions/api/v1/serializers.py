from rest_framework import serializers

from apps.transactions.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["user", "product", "quantity"]

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than zero!")
        return value

    def create(self, validated_data):
        product = validated_data.get("product")
        quantity = validated_data.get("quantity")
        amount = product.price * quantity
        validated_data["amount"] = amount
        return super().create(validated_data)
