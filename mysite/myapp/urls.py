from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.success, name='success'),
    path('monitor/', views.monitor, name='monitor'),
    path('delete_event/<event_id>', views.delete_event, name='delete_event'),
    path('delete_all_event/', views.delete_all_event, name='delete_all_event'),
    path('mark_event/<event_id>', views.mark_event, name='mark_event'),
    path('mark_all_event/', views.mark_all_event, name='mark_all_event'),
    path('mark_event_x/<event_id>', views.mark_event_x, name='mark_event_x'),
]