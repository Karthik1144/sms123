from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login1,name='login1'),
    # path('logout/',views.logout,name='logout'),
    path('photo/', views.photo, name='photo'),
    path('base/', views.base, name='base'),
    path('homepage/', views.homepage, name='homepage'),
    path('UserRegisterPageCall/', views.UserRegisterPageCall, name='UserRegisterPageCall'),
    path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('login_user/',views.login_user,name='login_user'),
    path('logout/',views.logout,name='logout'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),

  ]