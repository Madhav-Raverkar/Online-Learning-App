from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [

    path('', views.home, name = "home"),
    path("<int:id>/show", views.show_blog, name='show'),
    path("<int:id>/<int:id1>/update", views.update_blog, name='update'),
    path("<int:id>/<int:id1>/delete", views.delete_blog, name='delete'), 
    path("<int:id>/<int:pk>/add_blog", views.add_blog,  name="add_blog"),
    path("signup/", views.register, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path('contact/', views.contact, name = "contact"),
]