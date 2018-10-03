from django.contrib.auth import views

class LoginView(views.LoginView):
    template_name = 'auth/login.html'

class LogoutView(views.LogoutView):
    next_page = '/'