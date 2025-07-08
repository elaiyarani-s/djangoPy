from django.shortcuts import render
from .forms import BasicForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
        
            # Process the data in  form.cleaned_data
            # For now, we will just render the same page with a success message
            return render(request, 'basicapp/form_page.html', {'form': form, 'success': True})
    else:
        form = BasicForm()
    return render(request, 'basicapp/index.html', {'form': form})

def form_page(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'basicapp/form_page.html', {'form': form, 'success': True})
    else:
        form = BasicForm()

    return render(request, 'basicapp/form_page.html', {'form': form})
# def success(request):
    # return render(request, 'basicapp/success.html')