from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^removeTask$', views.DeleteTaskView.as_view(), name="delete_task"),
    url(r'$', views.TaskView.as_view(), name="tasks"),
    
]
