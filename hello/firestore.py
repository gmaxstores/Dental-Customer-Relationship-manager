from .firebase import db
from datetime import datetime




def create_patient(data):
    data['created_at'] = datetime.utcnow()
    db.collection('patients').add(data)




def get_patients():
    return [doc.to_dict() | {'id': doc.id} for doc in db.collection('patients').stream()]




def get_patient(patient_id):
    doc = db.collection('patients').document(patient_id).get()
    return doc.to_dict() | {'id': doc.id} if doc.exists else None




def create_appointment(data):
    db.collection('appointments').add(data)

def get_appointments_for_patient(patient_id):
    return [
        doc.to_dict() | {'id': doc.id}
        for doc in db.collection('appointments')
        .where('patient_id', '==', patient_id)
        .stream()
    ]

def get_all_appointments():
    appointments = []

    for doc in db.collection("appointments").stream():
        appointment = doc.to_dict()
        appointment["id"] = doc.id

        patient_id = appointment.get("patient_id")

        # Fetch patient document
        patient_doc = db.collection("patients").document(patient_id).get()

        if patient_doc.exists:
            patient = patient_doc.to_dict()
            appointment["patient_first_name"] = patient.get("first_name")
            appointment["patient_last_name"] = patient.get("last_name")
        else:
            appointment["patient_first_name"] = "Unknown"
            appointment["patient_last_name"] = ""

        appointments.append(appointment)

    return appointments


def update_appointment(appointment_id, data):
    db.collection('appointments').document(appointment_id).update(data)

def delete_appointment(appointment_id):
    db.collection('appointments').document(appointment_id).delete()


def get_appointment(appointment_id):
    doc = db.collection("appointments").document(appointment_id).get()
    if doc.exists:
        return doc.to_dict() | {"id": doc.id}
    return None

def delete_patient(patient_id):
    db.collection('patients').document(patient_id).delete()