from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from api.models import Document
from api.forms import RetrieveForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

class Retrieve(View):
    def get(self, request):
        form = RetrieveForm()
        context = {"form": form}
        return render(request, 'retrieve.html', context)

    def post(self, request):
        if request.method == "POST":
            print(request.POST)
            form = RetrieveForm(request.POST, request.FILES)
            if form.is_valid():
                rut = request.POST["rut"]
                password = request.POST["password"]
                #form.save()
                try:
                    doc = Document.objects.get(password=password, user=User.objects.get(username=rut))
                    return render(request, "succesfull.html", {"password": doc.dispenser_slot})
                except ObjectDoesNotExist:
                    form = RetrieveForm()
                    messages.error(request, "No matching document found.")           
        else:
            form = RetrieveForm()

        return render(request, "retrieve.html", {"form": form})