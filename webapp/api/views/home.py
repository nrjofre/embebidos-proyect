from django.shortcuts import render
from django.views import View

class Home(View):
    def get(self, request):
        context = {}
        return render(request, 'home.html', context)