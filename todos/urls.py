from django.urls import path
from .views import IndexList, TodoCreate, TodoToggle, TodoDelete, ListAdd, ListDelete

urlpatterns = [
    path('', IndexList, name='index-list'),

    # ITEMS
    path('add/', TodoCreate.as_view(), name='todo-add'),
    path('toggle/<int:pk>/', TodoToggle.as_view(), name='todo-toggle'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name='todo-delete'),

    # LISTS
    path('add-list/', ListAdd.as_view(), name='list-add'),
    path('delete-list/<int:pk>/', ListDelete.as_view(), name='list-delete'),

]
