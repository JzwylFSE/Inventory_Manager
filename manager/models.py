from django.db import models
from django.utils import timezone
from django.utils.html import format_html

class Record(models.Model): 
    # A log of items collected from ICT office
    date = models.DateField(default=timezone.now)
    name = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    time_in = models.TimeField(default=timezone.now)
    time_out = models.TimeField(blank=True, null=True)
    
    def is_returned(self):
        """Return True/False for logic"""
        return bool(self.time_out)
    is_returned.boolean = True
    
    def status_badge(self):
        """Custom badge for admin panel"""
        if self.time_out:
            return format_html('<span style="color: white; background: green; padding: 3px 6px; border-radius: 4px;">Returned</span>')
        return format_html('<span style="color: white; background: red; padding: 3px 6px; border-radius: 4px;">Not Returned</span>')
    status_badge.short_description = "Status"
    
    class Meta:
        ordering = ['-date', '-time_in']
        
    def __str__(self):
        return f"{self.name} → {self.item} ({'Returned' if self.time_out else 'Not Returned'})"
