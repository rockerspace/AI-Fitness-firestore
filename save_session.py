import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# Initialize Firebase
cred = credentials.Certificate("/Users/narendravenkatesan/Desktop/ai-fitness-tracker/my-project-21f4c-firebase-adminsdk-fbsvc-667f387075.json")
firebase_admin.initialize_app(cred)

# Firestore client (initialize db properly here)
db = firestore.client()

# Example session data (replace with dynamic data from your app)
session_data = {
    'user_id': 'user123',
    'exercise': 'Push-ups',
    'reps': 20,
    'sets': 3,
    'timestamp': firestore.SERVER_TIMESTAMP,  # Timestamp of when the data is added
    'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Current date and time
}

# Save the session data to a Firestore collection
try:
    db.collection('sessions').add(session_data)
    print("Session data saved to Firestore successfully.")
except Exception as e:
    print(f"Error saving session data: {e}")
