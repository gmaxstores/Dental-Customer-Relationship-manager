from django.urls import path
from hello import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/add/', views.patient_create, name='patient_create'),
    path('patients/<str:patient_id>/', views.patient_detail, name='patient_detail'),
    path('patients/<str:patient_id>/appointments/add/', views.appointment_create, name='appointment_create'),
    path('appointments/<str:appointment_id>/edit/', views.edit_appointment, name='edit_appointment'),
    path(
        "appointments/<str:appointment_id>/delete/",
        views.delete_appointment_view,
        name="delete_appointment"
    ),
    path(
        'patients/<str:patient_id>/delete/',
        views.patient_delete,
        name='patient_delete'
    ),
]
