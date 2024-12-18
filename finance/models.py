# region				-----External Imports-----
from django.db import models
# endregion

# region				-----Internal Imports-----
from . import choices as finance_choices
# endregion

# region			  -----Supporting Variables-----
# endregion


class Expense(models.Model):

    user = models.ForeignKey(to='user.User', on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=50, choices=finance_choices.CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.title} - {self.amount} ({self.category})"