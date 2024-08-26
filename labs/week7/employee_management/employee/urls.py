from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='employee'),
    path('position', views.position, name='position'),
    path('project', views.ProjectView.as_view(), name='project'),
    path('project/<int:id>', views.ProjectView.as_view(), name='project_id'),
    path('project/<int:id>/staff/<int:eid>', views.ProjectStaffView.as_view(), name='project_id_staff_eid'),
    path('project_details/<int:id>', views.project_detail, name='project_detail'),
]
