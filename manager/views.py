from django.shortcuts import render, redirect, get_object_or_404
from .models import Record
from .forms import RecordForm
from django.utils import timezone
from django.http import HttpResponse

def home(request):
    if request.method == "POST":
        if "return_id" in request.POST:
            # Returning (set time_out)
            record = Record.objects.get(id=request.POST.get("return_id"))
            record.time_out = timezone.localtime().time()
            record.save()
            return redirect("home")
        else:
            # Creating a new record
            form = RecordForm(request.POST)
            if form.is_valid():
                record = form.save(commit=False)
                record.time_in = timezone.localtime().time()   # ✅ Set time_in here
                record.save()
                return redirect("home")
    else:
        form = RecordForm()

    records = Record.objects.all().order_by("-date", "id")
    return render(request, "index.html", {"form": form, "records": records})
