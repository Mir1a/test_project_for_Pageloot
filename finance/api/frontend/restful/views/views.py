# region -----External Imports-----
from datetime import datetime

from django.db.models import Sum
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# endregion


# region -----Internal Imports-----
from ..... import models as finance_models
from .. import serializers as finance_serializers
# endregion

# region -----Supporting Variables-----
# endregion


@extend_schema(
    tags=['Expense'],
    description="Operations related to expenses."
)
class ExpenseViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = finance_models.Expense.objects
    serializer_class = finance_serializers.ExpenseSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter('user_id', str, description="User ID", required=True),
            OpenApiParameter('start_date', str, description="Start date in YYYY-MM-DD format", required=True),
            OpenApiParameter('end_date', str, description="End date in YYYY-MM-DD format", required=True)
        ]
    )
    @action(detail=False, methods=['get'])
    def list_by_date_range(self, request):
        user_id = request.query_params.get('user_id')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if not start_date or not end_date:
            return Response({"detail": "start_date and end_date are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        except ValueError:
            return Response({"detail": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        expenses = self.get_queryset().filter(user_id=user_id, date__range=[start_date, end_date])
        serializer = finance_serializers.ListByDateRangeSerializer(expenses, many=True)
        return Response(serializer.data)

    @extend_schema(
        parameters=[
            OpenApiParameter('user_id', str, description="User ID", required=True),
            OpenApiParameter('month', int, description="Month of the year", required=True),
            OpenApiParameter('year', int, description="Year", required=True)
        ]
    )
    @action(detail=False, methods=['get'])
    def category_summary(self, request):
        user_id = request.query_params.get('user_id')
        month = request.query_params.get('month')
        year = request.query_params.get('year')

        if not month or not year:
            return Response({"detail": "month and year are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            month = int(month)
            year = int(year)
            if month < 1 or month > 12:
                raise ValueError
        except ValueError:
            return Response({"detail": "Invalid month or year."}, status=status.HTTP_400_BAD_REQUEST)

        start_date = datetime(year, month, 1)
        end_date = datetime(year, month + 1, 1) if month < 12 else datetime(year + 1, 1, 1)
        print(start_date)
        print(end_date)

        expenses = self.get_queryset().filter(user_id=user_id, date__range=[start_date, end_date])
        category_summary = (
            expenses.values('category')
            .annotate(total_amount=Sum('amount'))
            .order_by('category')
        )

        summary_data = [
            {'category': entry['category'], 'total_amount': entry['total_amount']}
            for entry in category_summary
        ]
        return Response(summary_data)
