from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic.edit import CreateView

# Create your views here.
#def home_view(request):
#   return render(request,'booking/index.html')
    

class Home(generic.DetailView):
    """
    Renders the Index page in the browser
    """
    def get(self, request):
        return render(request, 'index.html')
