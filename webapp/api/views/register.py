from django.shortcuts import render, redirect
from api.forms import RegisterForm
from django.views import View
from django.contrib.auth.models import User

# Create your views here.
class Register(View):
    def post(self, request):
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                username = request.POST["username"]
                form.save()
                user = User.objects.get(username=username) # para creacion de perfil
                return redirect("/")
        else:
            form = RegisterForm()
            
        return render(request, "register/register.html", {"form": form})

    def get(self, request):
        form = RegisterForm()
        return render(request, "register/register.html", {"form": form})
