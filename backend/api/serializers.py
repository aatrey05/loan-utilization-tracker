from rest_framework import serializers

class BeneficiarySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=False)
    phone = serializers.CharField(max_length=15)
    loan_amount = serializers.FloatField(required=False)

class UploadSerializer(serializers.Serializer):
    beneficiary_phone = serializers.CharField(max_length=15)
    file_base64 = serializers.CharField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    approved = serializers.BooleanField(default=False)
