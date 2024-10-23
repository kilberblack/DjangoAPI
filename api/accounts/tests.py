import os
import django
from django.conf import settings

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoAPI.settings')  # Replace 'your_project_name' with your actual project name

# Setup Django
django.setup()

# Now you can import DRF
try:
    from rest_framework import serializers
    from rest_framework.views import APIView
    print("DRF imports successful!")
except ImportError as e:
    print(f"Error importing DRF: {e}")