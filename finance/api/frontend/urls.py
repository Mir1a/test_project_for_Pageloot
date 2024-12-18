# region				-----External Imports-----
from rest_framework import routers
from .restful import views as edition_views
# endregion

# region				-----Internal Imports-----
# endregion

# region			  -----Supporting Variables-----
# endregion

finance_router = routers.DefaultRouter()
finance_router.register(prefix='frontend/Expense', viewset=edition_views.ExpenseViewSet, basename='Expenses')
