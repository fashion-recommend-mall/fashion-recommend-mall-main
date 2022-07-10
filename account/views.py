from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from account.forms import LoginForm

# Create your views here.


# Create your views here.
def login_view(request):

    form = LoginForm(request.POST or None)
    msg = None
    
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'
        
    return render(request, "login.html", {"form": form, "msg": msg})

    