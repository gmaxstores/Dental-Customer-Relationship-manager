# hello/firebase.py
import os
import firebase_admin
from firebase_admin import credentials, firestore
from django.conf import settings

cred = credentials.Certificate(
    os.path.join(settings.BASE_DIR, "dental-crm-d977a-firebase-adminsdk-fbsvc-856263c614.json")
)

firebase_admin.initialize_app(cred)
db = firestore.client()
