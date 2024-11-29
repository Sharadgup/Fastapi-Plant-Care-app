# backend/firebase_config.py
import firebase_admin
from firebase_admin import credentials, firestore, storage
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Initialize Firebase Admin
cred = credentials.Certificate(os.getenv('FIREBASE_KEY_PATH'))
firebase_admin.initialize_app(cred, {
    'storageBucket': os.getenv('FIREBASE_BUCKET_URL')
})

# Firebase Firestore and Storage Client
db = firestore.client()
bucket = storage.bucket()
