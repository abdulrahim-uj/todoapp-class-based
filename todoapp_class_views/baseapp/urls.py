from django.urls import path
from . import views

app_name = "baseapp"

urlpatterns = [
    path('', views.TasksListView.as_view(), name="home"),
    path('create/', views.TaskCreateView.as_view(), name="create"),
    path('detail-view/<int:pk>/', views.TaskDetailView.as_view(), name="detail_view"),
    path('update-detail-view/<int:pk>/', views.TaskUpdateView.as_view(),
         name="update_view"),
    path('delete-task/<int:pk>/', views.TaskDeleteView.as_view(), name="delete_view"),
]
