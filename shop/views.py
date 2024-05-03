from django.shortcuts import render

# Create your views here.
def home_view(request):
    """View returning the index page"""
    return render(request, 'index.html')

def menu_view(request):
        return render(request, 'menu.html')