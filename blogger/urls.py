from django.urls import path
from .views import home_view, create_view, list_view, login_view, logout_view, signup_view, index_view, profile_view, edit_view
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('index/', index_view, name='index'),
    path('home/', home_view, name='home'),
    path('create/', create_view, name='create'),
    path('list/', list_view, name='list'),
    path('profile/', profile_view, name='profile'),
    path('edit/', edit_view, name='edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)