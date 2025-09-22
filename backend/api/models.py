from django.db import models

# Beneficiary model
class Beneficiary(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.mobile_number})"


# Uploads made by beneficiaries
class Upload(models.Model):
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE, related_name="uploads")
    file_url = models.URLField()  # URL of uploaded photo/video
    description = models.TextField(blank=True, null=True)
    approved = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Upload {self.id} by {self.beneficiary.name}"


# OTPs for mobile verification
class OTP(models.Model):
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE, related_name="otps")
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"OTP {self.otp_code} for {self.beneficiary.mobile_number}"
