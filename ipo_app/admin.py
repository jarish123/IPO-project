# ipo_app/admin.py

from django.contrib import admin
from .models import IPO

@admin.register(IPO)
class IPOAdmin(admin.ModelAdmin):
    list_display = (
        'company_name', 'status', 'open_date', 'close_date',
        'issue_size', 'ipo_price', 'listing_price',
        'get_listing_gain', 'get_cmp', 'get_current_return'
    )

    @admin.display(description='Listing Gain')
    def get_listing_gain(self, obj):
        return obj.listing_gain

    @admin.display(description='CMP')
    def get_cmp(self, obj):
        return obj.cmp

    @admin.display(description='Current Return (%)')
    def get_current_return(self, obj):
        return obj.current_return
