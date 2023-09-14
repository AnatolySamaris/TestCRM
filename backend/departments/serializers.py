from rest_framework import serializers

from .models import Department, DepartmentMember

from tasks.serializers import TaskSerializer


class DepartmentMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentMember
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    members = DepartmentMemberSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        exclude = ["tasks"]


class DepartmentTasksSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        exclude = ["members"]
