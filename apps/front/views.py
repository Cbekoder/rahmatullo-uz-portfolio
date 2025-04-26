from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Entrepreneur, Business, CoreValue, PortfolioItem
from .forms import ContactForm


def home(request):
    # Get data from models
    entrepreneur = Entrepreneur.objects.first()
    businesses = Business.objects.all()
    core_values = CoreValue.objects.all()
    portfolio_items = PortfolioItem.objects.all()

    # Handle contact form
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Xabaringiz uchun rahmat! Tez orada siz bilan bog'lanamiz.")
            return redirect('home')
    else:
        form = ContactForm()

    # Prepare categories for portfolio filtering
    categories = ['All'] + list(set([item.category for item in portfolio_items]))

    context = {
        'entrepreneur': entrepreneur,
        'businesses': businesses,
        'core_values': core_values,
        'portfolio_items': portfolio_items,
        'categories': categories,
        'form': form,
    }

    return render(request, 'index.html', context)
