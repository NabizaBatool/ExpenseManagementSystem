from django.contrib import admin

from expensesystem.models import *

# Register your models here.
admin.site.register(Expense)

admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Income)

