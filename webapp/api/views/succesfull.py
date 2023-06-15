from django.shortcuts import render
from django.views import View

class Succesfull(View):
    def get(self, request, password):
        context = {}
        return render(request, 'succesfull.html', password)