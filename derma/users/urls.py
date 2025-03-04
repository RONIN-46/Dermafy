from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views
from .views import home, user_login, user_logout, user_signup,edit_profile, delete_profile

urlpatterns =[
        path('',home,name='home'),
        path('user_login/',user_login, name='user_login'),
        path('user_logout/',user_logout,name='user_logout'),
        path('user_signup',user_signup,name='user_signup'),
        path("quiz/", submit_quiz, name="submit_quiz"),
        path('edit-profile/', edit_profile, name='edit_profile'),
        path('delete-profile/', delete_profile, name='delete_profile'),
        path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"), 
         name='password_reset'),
        path('password-reset/done/', 
                auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), 
                name='password_reset_done'),
        path('password-reset-confirm/<uidb64>/<token>/', 
                auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), 
                name='password_reset_confirm'),
        path('password-reset-complete/', 
                auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), 
                name='password_reset_complete'),
        path("request-otp/", request_otp, name="request_otp"),
        path("verify-otp/", verify_otp, name="verify_otp"),

        ]




    





    


   
    