from django.shortcuts import render
from requests import request
from app1.serializers import *
from accounts.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from app1.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.

class CertificateViewAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    """
    List all Certificate.
    """
    def get(self, request, format=None):
        Certificate = certificate.objects.all()
        serializer = CertificateSerializer(Certificate, many=True)
        return Response(serializer.data)


class UserCertificateListCreateAPIView(generics.ListCreateAPIView):
    """
    List all UserCertificate, or create a new UserCertificate.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    queryset = usercertificate.objects.all()
    serializer_class = UserCertificateSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

    def get_queryset(self):
        queryset = usercertificate.objects.filter(user_id = self.request.user)
        return queryset

class UserCertificatetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a UserCertificate instance.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    queryset = usercertificate.objects.all()
    serializer_class = UserCertificateSerializer

    def get_queryset(self):
        queryset = usercertificate.objects.filter(user_id = self.request.user)
        return queryset

    # def get_object(self, pk):
    #     try:
    #         return usercertificate.objects.get(pk=pk)
    #     except usercertificate.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk, format=None):
    #     UserCertificate = self.get_object(pk)
    #     serializer = UserCertificateSerializer(UserCertificate)
    #     return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     UserCertificate = self.get_object(pk)
    #     serializer = UserCertificateSerializer(UserCertificate, data=request.data, context={'request':request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     UserCertificate = self.get_object(pk)
    #     UserCertificate.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class JobType(generics.ListAPIView):
    queryset = jobtype.objects.all()
    serializer_class = JobtypeSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,]


class JobList(generics.ListAPIView):
    queryset = jobs.objects.all()
    serializer_class = JobsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,]

    def get(self, request, format=None):
        job = jobs.objects.filter(user_id = self.request.user)
        serializer = self.serializer_class(job, many=True)
        return Response(serializer.data, status.HTTP_200_OK) 
    
class JobCreate(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,]

    queryset = jobs.objects.all()
    serializer_class = JobsSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

class JobassignmentAPIView(APIView):
    serializer_class = JobassignmentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def post(self, request, pk):
        data = request.data
        print(data)
        print(pk)
        # job_assignment_obj = jobassignment.objects.filter(job_id = pk, assigned_to = data['assigned_to'], owner = self.request.user)
        data._mutable = True
        data["job_id"] = pk
        data._mutable = False
        serializer = self.serializer_class(data = data)
        serializer.is_valid(raise_exception = True)
        serializer.save(user_id=request.user)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def get(self, request, pk, format=None):
        assignments = jobassignment.objects.filter(job_id=pk).exclude(assignment_status="unassigned")
        serializer = self.serializer_class(assignments, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

class JobassignmentUnassignEmployee(APIView):
    serializer_class = JobassignmentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def put(self, request, assignment_id):
        try:
            assignment = jobassignment.objects.get(id=assignment_id)
            serializer = self.serializer_class(assignment, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                serializer_data = serializer.data
                return Response(serializer_data, status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except jobassignment.DoesNotExist:
            return Response({'errors': 'assignment does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
class NotesEmployeeAPIView(APIView):
    serializer_class = NotesSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def post(self, request, pk):
        try:
            assignment = jobassignment.objects.exclude(assignment_status='unassigned').get(assigned_to = request.user, id=pk)
            print(assignment)
        except:
            return Response({'error': 'This job is not available!'}, status.HTTP_400_BAD_REQUEST)
        
        data = request.data
        print(data)
        data._mutable = True
        data['job_assignment_id']=pk
        data.mutable = False
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request, pk):
        try:
            assignment = jobassignment.objects.exclude(assignment_status='unassigned').get(assigned_to = request.user, id=pk)
            print(assignment)
        except:
            return Response({'error': 'This job is not available!'}, status.HTTP_400_BAD_REQUEST)
        allnotes = notes.objects.filter(job_assignment_id=pk)
        count = len(allnotes)
        serializer = self.serializer_class(allnotes, many=True)
        return Response(
            {
                'success': True,
                'data' : serializer.data,
                'status_code' : status.HTTP_202_ACCEPTED,
                'count' : count
            }
        )

class NotesEmployerView(generics.CreateAPIView):
    serializer_class = NotesSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        








