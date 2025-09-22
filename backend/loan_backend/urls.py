"""
URL configuration for loan_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import BeneficiaryView, UploadView, ApproveUploadView, VerifyOTPView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/beneficiaries/', BeneficiaryView.as_view(), name='beneficiaries'),
    path('api/uploads/', UploadView.as_view(), name='uploads'),
    path('api/uploads/approve/<str:upload_id>/', ApproveUploadView.as_view(), name='approve-upload'),
    path('api/verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
]
