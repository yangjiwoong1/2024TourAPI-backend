# planners/serializers.py
from rest_framework import serializers
from datetime import datetime
from .models import Plan, Destination
from django.contrib.auth import get_user_model

User = get_user_model()

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'creator', 'title', 'start_date', 'end_date', 'created_at', 'updated_at']

    def validate_start_date(self, value):
        end_date = datetime.strptime(self.initial_data.get('end_date'), '%Y-%m-%d').date()
        if value > end_date:
            raise serializers.ValidationError("시작일이 종료일보다 늦습니다.")
        return value

    def validate_end_date(self, value):
        start_date = datetime.strptime(self.initial_data.get('start_date'), '%Y-%m-%d').date()
        if value < start_date:
            raise serializers.ValidationError("종료일이 시작일보다 이릅니다.")
        return value

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['id', 'plan', 'content_id', 'content_title', 'custom_name', 'gpsX', 'gpsY', 'visit_date', 'visit_time']
