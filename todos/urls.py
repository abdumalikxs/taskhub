from django.urls import path
from .views import IndexList, TodoCreate, TodoToggle, TodoDelete, ListAdd, ListDelete, TodoEdit
# ListEdit
urlpatterns = [
    path('', IndexList, name='index-list'),

    # ITEMS
    path('add/', TodoCreate.as_view(), name='todo-add'),
    path('toggle/<int:pk>/', TodoToggle.as_view(), name='todo-toggle'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name='todo-delete'),
    path('edit/<int:pk>/', TodoEdit.as_view(), name='todo-edit'),

    # LISTS
    path('add-list/', ListAdd.as_view(), name='list-add'),
    path('delete-list/<int:pk>/', ListDelete.as_view(), name='list-delete'),
    # path('delete-list/<int:pk>/', ListEdit.as_view(), name='list-edit'),

]
