from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calc/', views.calc),
    path('cadastroC/', views.cadastro),
    path('cadastroU/', views.cadastroU),
    path('cadastroF/', views.cadastroF),
    path('cadastroP/', views.cadastroP),
    path('cadastroV/', views.cadastroV),
    path('success/', views.success),
    path('successC/', views.successC),
    path('unsuccessC/', views.unsuccessC),
    path('unsuccessF/', views.unsuccessF),
    path('unsuccessU/', views.unsuccessU),
    path('unsuccessV/', views.unsuccessV),
]