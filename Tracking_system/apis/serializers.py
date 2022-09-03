# from rest_framework import serializers
# from apis.models import *


# class CertificatelevelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = certificatelevel
#         fields = (
#             'id',
#             'level'
#             )

# class CertificateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = certificate
#         fields = (
#             'id',
#             'levelofcertificate',
#             'title'
#             )

# class UserCertificateSerializer(serializers.ModelSerializer):
#     user_id = serializers.ReadOnlyField(source='user_id.username')
#     class Meta:
#         model = usercertificate
#         fields = (
#             'id',
#             'user_id',
#             'certificate_id',
#             'file_path',
#             'issue_date',
#             'expire_date'
#         )
