from django.urls import path
from .views import home, create_view, list_view, login_view, logout_view, signup_view,\
        index_view, ProfileView,edit_view , blog_edit_view, delete_blog_view
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('index/', index_view, name='index'),
    path('home/', home, name='home'),
    path('create/', create_view, name='create'),
    path('list/', list_view, name='list'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit/<int:user_id>/', edit_view, name='edit'),
    path('blog-edit/<int:user_id>/', blog_edit_view, name='blog-edit'),
    path('blog-delete/<int:user_id>/',delete_blog_view, name='deletet'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)