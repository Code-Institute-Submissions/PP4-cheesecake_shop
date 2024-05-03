from django.shortcuts import render

# Create your views here.
def home_view(request):
    """View returning the index page"""
    return render(request, 'shop/index.html', context)