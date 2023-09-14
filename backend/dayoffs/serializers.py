from rest_framework import serializers

from .models import Dayoff


class DayoffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dayoff
        fields = "__all__"
