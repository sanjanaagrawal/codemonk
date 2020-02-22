from django.urls import path
from firstapp import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',user_views.index,name='index'),
    path('ind/',user_views.ind,name='ind'),
    path('search/',user_views.search,name='search'),
    path('profile/',user_views.profile,name='profile'),
    path('addrecipe/',user_views.addrecipe,name='addrecipe'),
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
