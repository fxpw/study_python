from django.shortcuts import render

from .forms import ReqForm
from .models import Vacancy, Word, Wordskill
from hhapp.management.commands.full_db import Command


def start(request):
    return render(request, 'hhapp/index.html')


def form(request):
    form1 = ReqForm
    return render(request, 'hhapp/form.html', context={'form': form1})


def result(request):
    if request.method == 'POST':
        form = ReqForm(request.POST)
        if form.is_valid():
            vac = form.cleaned_data['vacancy']
            where = form.cleaned_data['where']
            pages = form.cleaned_data['pages']
            print(vac, where, pages, sep='\n')
            com = Command(vac, pages, where)
            com.handle()
            v = Word.objects.get(word=vac)
            s = Wordskill.objects.filter(id_word_id=v.id).all()
            vac = Vacancy.objects.filter(word_id=v).all()
            print(vac, v, s, sep='\n')
            return render(request, 'hhapp/about.html', context={'vac': vac, 'word': v, 'skills': s})
        else:
            form1 = ReqForm
            return render(request, 'hhapp/form.html', context={'form': form1})


