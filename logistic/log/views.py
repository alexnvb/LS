from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Count, F
from _datetime import datetime, timedelta, date
from .models import *
from .forms import *

# Create your views here.

class IndexHome(ListView):
    model = Record
    now = date.today()

    def get_context_data(self, *, object_list=None, **kwargs):
        now = date.today()
        context = super().get_context_data(**kwargs)
        context['date1'] = now - timedelta(days=1)
        context['date2'] = now
        context['date3'] = now + timedelta(days=1)
        context['date4'] = now + timedelta(days=2)
        context['date5'] = now + timedelta(days=3)
        context['date6'] = now + timedelta(days=4)
        return context

    def get_queryset(self):
        return Record.objects.filter(date_appointed__gte=date.today()-timedelta(days=1))


# def index(request):
#     now = datetime.now()
#     today = date.today()
#
#     date1 = now - timedelta(days=1)
#     date3 = now + timedelta(days=1)
#     date4 = now + timedelta(days=2)
#     date5 = now + timedelta(days=3)
#     date6 = now + timedelta(days=4)
#
#     rec1 = Record.objects.filter(date_appointed=date1)
#     rec2 = Record.objects.filter(date_appointed=now)
#     rec3 = Record.objects.filter(date_appointed=date3)
#     rec4 = Record.objects.filter(date_appointed=date4)
#     rec5 = Record.objects.filter(date_appointed=date5)
#     rec6 = Record.objects.filter(date_appointed=date6)
#
#     context = {
#         'rec1': rec1,
#         'rec2': rec2,
#         'rec3': rec3,
#         'rec4': rec4,
#         'rec5': rec5,
#         'rec6': rec6,
#         'now': now,
#         'date1': date1,
#         'date3': date3,
#         'date4': date4,
#         'date5': date5,
#         'date6': date6,
#
#     }
#     return render(request, 'log/index.html', context)

def record_view(request, record_id):
    record = get_object_or_404(Record, pk=record_id)

    context = {
        'record': record
    }
    return render(request, 'log/record_view.html', context)

def contractor_view(request, contractor_id):
    contractor = get_object_or_404(Contractor, pk=contractor_id)

    context = {
        'contractor': contractor
    }
    return render(request, 'log/contractor_view.html', context)

def add_record(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'log/add.html', {'form': form})