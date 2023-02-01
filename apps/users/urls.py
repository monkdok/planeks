from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include, reverse_lazy
from apps.users.forms import UserAuthenticationForm

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(**{
        'next_page': reverse_lazy('dummy_data:schema_list'),
        'template_name': 'users/login.html',
        'form_class': UserAuthenticationForm,
    }), name='login'),
    path('logout/', LogoutView.as_view(**{'next_page': reverse_lazy('dummy_data:schema_list')}), name='logout'),
]
