from django.shortcuts import render, redirect
from django.views import View  
from api.forms import DocumentForm
from django.contrib.auth.models import User
from ..models import Document
import random

class Newdoc(View):
    def get(self, request):
        form = DocumentForm()
        password = random.randint(100000, 999999)
        return render(request, "newdoc.html", {"form": form, "password": password})

    def post(self, request):
        if request.method == "POST":
            form = DocumentForm(request.POST, request.FILES)
            
            if form.is_valid():
                form.save()
                
                password = request.POST["password"]

                return render(request, "succesfull.html", {"password": password})
        else:
            form = DocumentForm()

        return render(request, "newdoc.html", {"form": form})

    def edit(request, doc_id):
        task = Document.objects.get(id=doc_id)
        form = DocumentForm(instance=task)
        if request.method == "POST":
            form = DocumentForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                doc_list = Document.objects.all()
                context = {'task_list': doc_list}
                return redirect('/')
        else:
            form = DocumentForm(instance=task)

        return render(request, "newdoc.html", {"form": form})