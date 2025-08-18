from django.db import models
from django.utils import timezone

# Create your models here.
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
        return f"{self.item} is returned at {self.time_out}" 

    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return f"Dr.{self.name} is with {self.item} at {self.location}"
    
    