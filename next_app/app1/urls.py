from django.urls import path
from app1.views import *

urlpatterns = [

    path('certificate/',CertificateViewAPIView.as_view()),

    path('usercertificate/',UserCertificateListCreateAPIView.as_view()),

    path('usercertificate/<int:pk>/',UserCertificatetDetail.as_view()),

    path('jobtype/', JobType.as_view()),

    path('joblist/', JobList.as_view()),

    path('jobcreate/',JobCreate.as_view()),

    path('job/<int:pk>/assignment/', JobassignmentAPIView.as_view()),

    path('job/assignment/<int:assignment_id>/', JobassignmentUnassignEmployee.as_view()),

    path('notes/assignment/<int:pk>/employee/', NotesEmployeeAPIView.as_view()),

    path('notes/employer/<int:pk>/', NotesEmployerView.as_view),
  
]