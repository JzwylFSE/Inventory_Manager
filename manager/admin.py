from django.contrib import admin
from django.utils.html import format_html
from .models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "name",
        "item",
        "location",
        "phone_number",
        "time_in",
        "time_out",
        "status_badge",
    )
    list_filter = ("date", "item", "location")
    search_fields = ("name", "item", "phone_number", "location")
    list_editable = ("time_out",) 
    list_display_links = ("name", "item", "location")
    fields = ("date", "name", "item", "location", "phone_number", "time_in", "time_out")
    # readonly_fields = ("time_in",)

    def status_badge(self, obj):
        """Show colored badge for return status in admin."""
        if obj.time_out:
            return format_html(
                '<strong style="color: #fff; background: #22c55e; padding: 3px 10px; border-radius: 6px; font-size: 12px;">Returned</strong>'
            )
        return format_html(
            '<strong style="color: #fff; background: #ef4444; padding: 3px 10px; border-radius: 6px; font-size: 12px;">Not Returned</strong>'
        )
    status_badge.allow_tags = True
    status_badge.short_description = "Status"
