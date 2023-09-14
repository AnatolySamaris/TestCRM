from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class PeriodEmployeeStatisticsSerializer(serializers.ModelSerializer):
    total_payment = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ["user", "hourly_rate", "hours", "total_payment"]
    
    def get_total_payment(self, obj):
        return str(obj.hourly_rate * obj.hours)
