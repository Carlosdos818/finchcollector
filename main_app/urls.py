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
    # Route to feeding model
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    # We need several urls for out Toys to work
    # we'll need a list, detail, create, update, delete
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete', views.ToyDelete.as_view(), name='toys_delete'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    # eventually, once it's all set up, we'll add two views to handle the relationship between a finch a toy.
    # Associate/Add a toy
    path('finches/<int:finch_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    # Unassociate/Remove a toy
    path('finches/<int:finch_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
]