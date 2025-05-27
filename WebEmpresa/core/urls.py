from django.urls import path
from core import views as core_views

urlpatterns = [
    path('home/', core_views.home, name='home'),
    path('about/', core_views.about, name='about'),
    path('store/', core_views.store, name='store'),        
    path('contact/', core_views.contact, name='contact'),    
    path('sample/', core_views.sample, name='sample'),       
]