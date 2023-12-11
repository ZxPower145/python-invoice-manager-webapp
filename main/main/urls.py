from django.contrib import admin
from django.urls import path
from ManagementSystem import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('add_invoice/', views.add_invoice, name='add_invoice'),
    path('show_invoices/', views.show_invoices, name='show_invoices'),
    path('update_invoice/<str:pk>/', views.update_invoice, name='update_invoice'),
    path('delete_invoice/<str:pk>/', views.delete_invoice, name='delete_invoice'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),
]
