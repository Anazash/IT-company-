from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.signup,name='signup'),
    path('about',views.about,name='about'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('services',views.services,name='services'),
    path('home',views.home,name='home'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('team',views.team,name='team'),

]
