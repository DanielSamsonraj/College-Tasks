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
    path('userProfile', views.viewProfile, name = "userProfile"),
    path('forgotPassword', views.forgotPassword, name = "forgotPassword"),
    path('enterOTP', views.enterOTP, name = "enterOTP"),
    path('setPassword', views.setPassword, name = "setPassword"),
    path('editProfile', views.editProfile, name = "editProfile"),
    path('accountDelete', views.accountDelete, name = "accountDelete"),
    path('changePassword', views.changePassword, name = "changePassword"),
    path('branch', views.groupByBranch, name = "branch"),
    path('year', views.groupByYear, name = "year"),
    path('section', views.groupBySection, name = "section"),
    path('allPosts', views.groupByAllPosts, name = "allPosts"),
    path('myPosts', views.groupByMyPosts, name = "myPosts"),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_URL)