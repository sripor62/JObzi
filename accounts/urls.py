from django.urls import path

from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

app_name='accounts'
urlpatterns=[
path('login1/',views.CompanyLoginView.as_view(),name='login1'),
path('login/',views.CustomLoginView.as_view(),name='login'),

path('logout/',views.CustomLogoutView.as_view(),name='logout'),
path('logout1/',views.CLogoutView.as_view(),name='logout1'),
path('signup/',views.SignUp.as_view(),name='signup'),
path('signup1/',views.CSignUp.as_view(),name='signup1'),
path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]
