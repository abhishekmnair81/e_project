from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('add-categories/', views.add_categories, name='add_categories'),
    path('', views.categories, name='categories'),
    path('products/<int:i>',views.products,name='products'),
    path('details/<int:i>',views.details,name='details'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('add-products/',views.add_products, name='add_products'),
    path('addstock/<int:i>', views.addstock, name='addstock'),

]