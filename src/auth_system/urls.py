from django.urls import path,include
from . import views
from django.contrib.auth     import views as auth



urlpatterns = [
    path('', views.home , name="home"),
    path('signup/', views.signUp , name="signUp"),
    path('login/', views.logIn , name="logIn"),
    path('logOut/',views.logOut , name='logOut'),
    path('adds/', views.Adds , name="Adds"),
    path('edite/', views.EditeUserInfo , name="EditeUserInfo"),
    path('creates/', views.CreateProfile , name="CreateProfile"),
    path('profile/', views.profile , name="profile"),






    path('change_password/', auth.PasswordResetView.as_view(template_name="pages/password_reset.html") , name="password_reset"),
    path('passord_confirm/', auth.PasswordResetDoneView.as_view(template_name="pages/password_sent.html"), name="password_reset_done"),
    path('password_sent/<uidb64>/<token>', auth.PasswordResetConfirmView.as_view(template_name="pages/password_form.html") , name="password_reset_confirm"),
    path('change_password_done/', auth.PasswordResetCompleteView.as_view(template_name="pages/password_done.html") , name="password_reset_complete"),
    


]
