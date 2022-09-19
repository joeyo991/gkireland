from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_charge', 'order_total',
                       'grand_total', 'original_basket',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'name',
              'email', 'phone', 'country',
              'town_or_city', 'address_line1',
              'address_line2', 'county', 'postcode',
              'delivery_charge', 'order_total', 'grand_total',
              'original_basket', 'stripe_pid')

    list_display = ('order_number', 'date', 'name',
                    'order_total', 'delivery_charge',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
