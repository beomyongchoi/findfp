from django.contrib import admin

# Register your models here.
from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subscription_date')
    search_fields = ['name']

admin.site.register(Subscription, SubscriptionAdmin)
