from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BeneficiarySerializer, UploadSerializer
from firebase_config import db
from firebase_admin import auth
import datetime

# Add a beneficiary
class BeneficiaryView(APIView):
    def post(self, request):
        serializer = BeneficiarySerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            db.collection('beneficiaries').document(phone).set(serializer.validated_data)
            return Response({"message": "Beneficiary added"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        beneficiaries = db.collection('beneficiaries').stream()
        result = [doc.to_dict() for doc in beneficiaries]
        return Response(result, status=status.HTTP_200_OK)

# Upload base64 images/videos
class UploadView(APIView):
    def post(self, request):
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            data['timestamp'] = datetime.datetime.utcnow().isoformat()
            db.collection('uploads').document().set(data)
            return Response({"message": "Upload saved"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Approve an upload
class ApproveUploadView(APIView):
    def patch(self, request, upload_id):
        doc_ref = db.collection('uploads').document(upload_id)
        if doc_ref.get().exists:
            doc_ref.update({'approved': True})
            return Response({"message": "Upload approved"}, status=status.HTTP_200_OK)
        return Response({"error": "Upload not found"}, status=status.HTTP_404_NOT_FOUND)

# OTP Login/Signup
class VerifyOTPView(APIView):
    def post(self, request):
        id_token = request.data.get('id_token')
        if not id_token:
            return Response({"error": "No ID token provided"}, status=400)
        try:
            decoded_token = auth.verify_id_token(id_token)
            phone_number = decoded_token['phone_number']

            # Check if user exists in Firestore
            user_ref = db.collection('beneficiaries').document(phone_number)
            if not user_ref.get().exists:
                # New user → create a record
                user_ref.set({
                    'phone': phone_number,
                    'created_at': datetime.datetime.utcnow().isoformat()
                })

            return Response({"message": "OTP verified", "phone": phone_number}, status=200)

        except Exception as e:
            return Response({"error": str(e)}, status=400)
