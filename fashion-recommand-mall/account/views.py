from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from account.forms import LoginForm, SignUpForm, UploadImageForm
from account.models import UserDetail
from account.service.get_sytle_service import get_style_service

# Create your views here.


# Create your views here.
def login_view(request):
    '''
    '''
    msg = None
    form = LoginForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/")
            msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'
        
    return render(request, "login.html", {"form": form, "msg": msg})


def logout_view(request):
    '''
    '''
    logout(request)
    return redirect("/")


@login_required(login_url="/account/login/")
def my_page_view(request):
    '''
    '''

    style_key_list = []
    style_value_list = []

    userDetail = UserDetail.objects.filter(user_id = request.user.id).first()

    for key in userDetail.__dict__:
        if key != "id" and key != "user_id" and key != "_state" and userDetail.__dict__.get(key) != 0:
            style_key_list.append(key)
            style_value_list.append(userDetail.__dict__.get(key))

    return render(request, "my-page.html", {"style_key_list": style_key_list,"style_value_list":style_value_list})


def register_view(request):
    '''
    '''
    msg = None
    sign_form = SignUpForm(request.POST or None)
    image_form = UploadImageForm(request.POST, request.FILES)

    if request.method == "POST":
        if sign_form.is_valid() and image_form.is_valid():
            files = request.FILES
            style_dict = get_style_service(files)

            admin_user=sign_form.save()
            user = UserDetail(user=admin_user, **style_dict)
            user.save()

            username = sign_form.cleaned_data.get("username")
            raw_password = sign_form.cleaned_data.get("password1")

            authenticate(username=username, password=raw_password)

            return redirect("/")
        else:
            msg = 'Form is not valid'

    return render(request, "register.html", {"sign_form": sign_form,"image_form":image_form ,"msg": msg})
