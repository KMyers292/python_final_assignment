from django.urls import path
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from .views import SignUp

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html.django'), name='login'),
    path('password_reset/', PasswordResetView.as_view(template_name='password_reset_form.html.django'), name='reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html.django'), name='reset-done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html.django'), name='reset-confirm'),
    path('reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_complete.html.django'), name='reset-complete'),
    path('signup/', SignUp.as_view(), name='signup'),
]