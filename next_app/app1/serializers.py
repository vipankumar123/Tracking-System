from rest_framework import serializers
from app1.models import *


class CertificatelevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = certificatelevel
        fields = (
            'id',
            'level'
            )

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = certificate
        fields = (
            'id',
            'levelofcertificate',
            'title'
            )

class UserCertificateSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.username')
    class Meta:
        model = usercertificate
        fields = (
            'id',
            'user_id',
            'certificate_id',
            'file_path',
            'issue_date',
            'expire_date'
        )

class JobtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobtype
        fields = (
            "id",
            'name'
        )

class JobsSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.username')
    class Meta:
        model = jobs
        fields = (
            'id',
            'user_id',
            'jobtype',
            'name',
            'description',
            'is_completed'
        )

class JobassignmentSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.username')
    class Meta:
        model = jobassignment
        fields = (
            'id',
            'user_id',
            'assigned_to',
            'job_id',
            'assign_time',
            'assignment_status',
            'completed_time'
        )

class NotesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user_id.username')
    class Meta:
        model = notes
        fields = (
            'id',
            'job_assignment_id',
            'description',
            'created_at',
            'owner',
            'job'
        )






