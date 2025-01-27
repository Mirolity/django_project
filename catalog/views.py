from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FeedbackForm


def home(request):
    return render(request, 'catalog/home.html')


def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Спасибо Вам за обращение!')
    else:
        form = FeedbackForm()
    return render(request, 'catalog/contact.html', {'form': form})
