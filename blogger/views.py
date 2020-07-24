from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import BlogForm
from .accounts import LoginForm, SignUpForm
from .models import UserDetail, BlogTable
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

USER = get_user_model()


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = authenticate(username=form.cleaned_data['username'],
                                email=form.cleaned_data['email'],
                                password=form.cleaned_data['password'],
                                )
            if user:
                login(request, user)
                return render(request, 'blogger/home.html')
            else:
                return HttpResponse("Your account was inactive.")

    elif request.method == 'GET':
        form = LoginForm()
        if request.user.is_authenticated:
            return redirect('/blog/home/')
        print('getttt')
        return render(request, 'blogger/login.html', {'form': form})


@login_required(login_url='/blog/login/')
def home_view(request):
    return render(request, 'blogger/home.html')


def logout_view(request):
    logout(request)
    return redirect('/blog/index')


def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        file_obj = request.FILES['myfile']
        if form.is_valid():
            print(form.cleaned_data)
            user = USER(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
            )
            fs = FileSystemStorage()
            fs.save(file_obj.name, file_obj)
            user.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/blog/login')
        else:
            return HttpResponse('error')
    elif request.method == 'GET':
        form = SignUpForm()
        return render(request, 'blogger/signup.html', {'form': form})


def index_view(request):
    return render(request, 'blogger/index.html')


# def register_form(request):
#     registered = False
#     user_details = Register()  # username, pass, email
#     bio_details = UserInfoForm()  # name , dob
#
#     if request.method == 'POST':
#         user_details = Register(request.POST)
#         bio_details = UserInfoForm(request.POST)
#
#         if user_details.is_valid() and bio_details.is_valid():
#             user_instance = user_details.save()
#             user_instance.set_password(user_instance.password)
#             user_instance.save()
#             profile = bio_details.save(commit=False)
#             profile.user = user_instance
#             profile.save()
#             registered = True
#             return redirect('/login/')
#
#         else:
#             print(user_details.errors, bio_details.errors)
#
#     return render(request, 'templates/register.html',
#                   {'user_details': user_details, 'bio_details': bio_details, 'pageTitle': 'Register Form'})
#

def create_view(request):
    blog_form = BlogForm()
    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            blog_form.save()
            print(request.POST)
            print("successfully saved")
            return redirect('/blog/home/')
        else:
            return HttpResponse("Form is not valid")
    return render(request, 'blogger/create.html/', {'form2': blog_form})


def list_view(request):
    model_form = BlogTable.objects.all()
    context = {
        'data': model_form,
    }
    return render(request, 'blogger/list.html/', context)


def profile_view(request):
    return render(request, 'blogger/profile.html/')


def edit_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, instance=UserDetail)
        if form.is_valid():
            print(form.cleaned_data)
            user = USER(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            user.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/blog/login')
        else:
            return HttpResponse('error')
    elif request.method == 'GET':
        form = SignUpForm(instance=UserDetail)
    return render(request, 'blogger/edit.html', {'form': form})
