from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name = "index"),
    path('teacherRegistration', views.teacherRegistration, name = "techerRegistration"),
    path('post', views.post, name = "post"),
    path('viewPosts', views.viewPosts, name = "viewPosts"),
    path('studentRegistration', views.studentRegistration, name = "studentRegistration"),
    path('login', views.login, name = "login"),
    path('logout', views.logout, name = "logout"),
    path('userProfile', views.viewProfile, name = "userProfile")

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_URL)