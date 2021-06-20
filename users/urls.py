from os import name
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # path('', views.home, name="home"),
    
    # path('register/', UserRegistrationView.as_view(), name="register" ),
    # path('edit_profile/', UserEditView.as_view(), name="edit_profile" ),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
     #path('reset_password/', views.MyPasswordResetView.as_view(), name="reset_password"),
    path('users/reset_password/', views.MyPasswordResetView.as_view(), name="reset_password"),
    #url(r'^api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/token/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    
]