import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
# Fetch the service account key JSON file contents
cred = credentials.Certificate('../app/service_account_firebase.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://plant-monitoring-n-controlling-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('raspberry-dev-1')
current_data = ref.child('plants')
current_data.set({
    'bayam': {
        'temperature': 312,
        'humidity': 12,
        'light_intensity' : 12,
        'soil_moisture' : 12,
        'status' : 'Optimal'
    },
    'seledri': {
        'temperature': 312,
        'humidity': 12,
        'light_intensity' : 12,
        'soil_moisture' : 12,
        'status' : 'Optimal'
    },
})

logs = ref.child('logs')
logs.push().set(
    {
        'name' : 'bayam',
        'temperature': 312,
        'humidity': 12,
        'light_intensity' : 12,
        'soil_moisture' : 12,
        'status' : 'Optimal',
        'time' : str(datetime.now())
    }
)

print(ref.get())
