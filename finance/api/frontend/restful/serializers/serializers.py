# region -----External Imports-----
from rest_framework import serializers
from user import models as user_models
# endregion

# region -----Internal Imports-----
from ..... import models as finance_models
# endregion

# region -----Supporting Variables-----
# endregion


class ExpenseSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=user_models.User.objects)

    class Meta:
        model = finance_models.Expense
        fields = ['id', 'user', 'title', 'amount', 'date', 'category']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Expense amount must be positive.")
        return value


class ListByDateRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = finance_models.Expense
        fields = ['id', 'title', 'amount', 'date', 'category']