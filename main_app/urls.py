from django.urls import path
from . import views
# this file is how we are going to map our urls to views 
# remember in django, views are like our controllers
# the `name='home'` is a kwag, that gives the route a name, naming routes is optional, but best practices 
# later on, we'll see just how useful this is.
urlpatterns = [
    path('', views.home, name='home'),
    # Route to about
    path('about/', views.about, name='about'),
    # Route for finches index
    path('finches/', views.finches_index, name='index'),
    # Route for the finches details
    path('finches/<int:finch_id>', views.finches_detail, name='detail'),
    # Route for create finch
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    # Route to update finch
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    # Route to delete finch
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),

]