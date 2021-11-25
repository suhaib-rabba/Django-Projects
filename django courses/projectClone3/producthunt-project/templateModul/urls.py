from django.urls import path, include
from templateModul import views

urlpatterns = [
    path('', views.home, name='templateModul'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_views, name='login'),
    path('forms/', views.modul_views,name='modul_url'),
    path('modulRender/', views.modul_render,name='modul_render_url'),
    path("<int:id>",  views.modul_detail , name='detail'),
    path('signup2/', views.signup2, name='signup2'),
    path('login2/', views.login_views2, name='login2'),



]
