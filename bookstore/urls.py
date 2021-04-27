
from django.urls import path
from .views import *


urlpatterns = [
   path('',LoginForm,name='login'),
   path('login/',LoginForm,name='login'),
    path('signup/', SignupForm,name='signup'),
    path('logout/', LogoutUser,name='logout'),
    path('dashboard/', UserDashboard,name='dashboard'),
path('add_new_book/', AddNewBook,name='add_book'),
path('delete_book/<int:bid>/', DeleteBook,name='delete_book'),
path('edit_book/<int:bid>/', EditBook,name='edit_book'),

]
