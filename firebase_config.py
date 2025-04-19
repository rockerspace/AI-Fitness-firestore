import firebase_admin
from firebase_admin import credentials, firestore

try:
    # Initialize Firebase with your service account credentials
    cred = credentials.Certificate('/Users/narendravenkatesan/Desktop/ai-fitness-tracker/my-project-21f4c-firebase-adminsdk-fbsvc-667f387075.json')  # Replace with the actual path to your serviceAccountKey.json
    firebase_admin.initialize_app(cred)

    # Initialize Firestore DB
    db = firestore.client()

    # Print confirmation if initialization succeeds
    print("Firebase initialized successfully.")
except Exception as e:
    print(f"Error initializing Firebase: {e}")
