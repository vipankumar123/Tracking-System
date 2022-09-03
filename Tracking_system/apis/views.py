# from django.shortcuts import render
# from apis.serializers import *
# from Accounts.serializers import *
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import generics
# from apis.permissions import IsOwnerOrReadOnly
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication


# # Create your views here.

# class CertificateViewAPIView(APIView):
#     """
#     List all Certificate.
#     """
#     def get(self, request, format=None):
#         Certificate = certificate.objects.all()
#         serializer = CertificateSerializer(Certificate, many=True)
#         return Response(serializer.data)


# class UserCertificateListCreateAPIView(generics.ListCreateAPIView):
#     """
#     List all UserCertificate, or create a new UserCertificate.
#     """
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
#     queryset = usercertificate.objects.all()
#     serializer_class = UserCertificateSerializer

#     def perform_create(self, serializer):
#         serializer.save(user_id=self.request.user)

#     def get_queryset(self):
#         queryset = usercertificate.objects.filter(user_id = self.request.user)
#         return queryset

# class UserCertificatetDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Retrieve, update or delete a UserCertificate instance.
#     """
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

#     queryset = usercertificate.objects.all()
#     serializer_class = UserCertificateSerializer

#     def get_queryset(self):
#         queryset = usercertificate.objects.filter(user_id = self.request.user)
#         return queryset

#     # def get_object(self, pk):
#     #     try:
#     #         return usercertificate.objects.get(pk=pk)
#     #     except usercertificate.DoesNotExist:
#     #         raise Http404

#     # def get(self, request, pk, format=None):
#     #     UserCertificate = self.get_object(pk)
#     #     serializer = UserCertificateSerializer(UserCertificate)
#     #     return Response(serializer.data)

#     # def put(self, request, pk, format=None):
#     #     UserCertificate = self.get_object(pk)
#     #     serializer = UserCertificateSerializer(UserCertificate, data=request.data, context={'request':request})
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(serializer.data)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # def delete(self, request, pk, format=None):
#     #     UserCertificate = self.get_object(pk)
#     #     UserCertificate.delete()
#     #     return Response(status=status.HTTP_204_NO_CONTENT)