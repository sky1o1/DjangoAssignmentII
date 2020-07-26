from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy

from .forms import BlogForm, AuthorForm, EditForm
from .accounts import LoginForm, SignUpForm
from .models import UserDetail, BlogTable
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.views.decorators.cache import cache_page
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template

USER = get_user_model()


# @cache_page(60)
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
def home(request):

    # html_file = get_template('blogger/mail_template.html')
    # html_content = html_file.render()
    # sub = 'Test'
    # from_email = 'test@gmail.com'
    # recipients = [request.user.email, ]
    # msg = EmailMultiAlternatives(subject=sub, from_email=from_email, to=recipients)
    # msg.attach_alternative(html_content, 'text/html')
    # msg.send()
    return render(request, 'blogger/home.html')


# class HomeView(TemplateView):
#     template_name = 'blogger/home.html'


def logout_view(request):
    logout(request)
    return redirect('/blog/index')


def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = USER(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
            )
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


# class Create(CreateView):
    # form_class = BlogForm
    # model = BlogTable
    # template_name = 'blogger/create.html'
    # success_url = reverse_lazy('blog:list')

def create_view(request):
    blog_form = BlogForm(request.POST)
    if request.method == 'POST':

        if blog_form.is_valid():
            instance = blog_form.save(commit=False)
            instance.author = request.user
            instance.save()
            print(request.POST)
            print("successfully saved")
            return redirect('/blog/list/')
        else:
            return HttpResponse("Form is not valid")
    else:
        return render(request, 'blogger/create.html/', {'form2': blog_form})


def list_view(request):
    model_form = BlogTable.objects.all()
    context = {
        'data': model_form,
    }
    return render(request, 'blogger/list.html/', context)


# class List(ListView):
#     model = BlogTable
#     template_name = 'blogger/list.html'
#     context_object_name = 'data'
#

class ProfileView(ListView):
    model = User
    template_name = 'blogger/profile.html'

    # return render(request, 'blogger/profile.html/')


def edit_view(request, user_id):
    obj1 = get_object_or_404(USER, id=user_id)
    # obj2 = get_object_or_404(UserDetail, id=user_id)

    if request.method == 'POST':
        form1 = AuthorForm(request.POST, instance=obj1)
        print('data', form1)
        # form2 = EditForm(request.POST, instance=obj2)
        if form1.is_valid():
            form1.save()
            return redirect('/blog/profile/')
        else:
            return HttpResponse('error')
    elif request.method == 'GET':
        print('test')
        form1 = AuthorForm(instance=obj1)
        form2 = EditForm()
    return render(request, 'blogger/edit.html', {'form1': form1, 'form2': form2})


# class ProfileEdit(UpdateView):
#     form_class = AuthorForm
#     pk_url_kwarg = 'user_id'
#     model = User, UserDetail
#     template_name = 'blogger/edit.html'
#     success_url = '/blog/profile/'


def blog_edit_view(request, user_id):
    bg = get_object_or_404(BlogTable, id=user_id)
    blog_form = BlogForm()
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, instance=bg)
        if blog_form.is_valid():
            instance = blog_form.save(commit=False)
            instance.author = request.user
            instance.save()
            print(request.POST)
            print("successfully saved")
            return redirect('/blog/list/')
        else:
            return HttpResponse("Form is not valid")
    else:
        blog_form = BlogForm(instance=bg)
    return render(request, 'blogger/create.html/', {'form2': blog_form})


# class BlogEdit(UpdateView):
#     form_class = BlogForm
#     model = BlogTable
#     pk_url_kwarg = 'user_id'
#     success_url = '/blog/list/'
#

def delete_blog_view(request, user_id):
    del_obj = get_object_or_404(BlogTable, id=user_id)
    del_obj.delete()
    return redirect('/blog/list/')

# class Delete(DeleteView):
#     model = BlogTable
#     success_url = '/blog/list'
#     pk_url_kwarg = 'user_id'
#


# def upload_view(request):
#     if request.method == 'POST':
#         form = EditForm(request.FILES['myfile'])
#         if form.is_valid():
#             form.save()
#         else:
#             return HttpResponse("error")
#     return render(request, 'blog/profile/', {'form': form})