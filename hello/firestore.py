from .firebase import db
from datetime import datetime



#function to create a new patient in the database
def create_patient(data):
    data['created_at'] = datetime.utcnow()
    db.collection('patients').add(data)



#function to get all patients from the database
def get_patients():
    return [doc.to_dict() | {'id': doc.id} for doc in db.collection('patients').stream()]



#function to get a single patient by id
def get_patient(patient_id):
    doc = db.collection('patients').document(patient_id).get()
    return doc.to_dict() | {'id': doc.id} if doc.exists else None



#function to update a patient's information
def create_appointment(data):
    db.collection('appointments').add(data)

#function to get all appointments for a specific patient
def get_appointments_for_patient(patient_id):
    return [
        doc.to_dict() | {'id': doc.id}
        for doc in db.collection('appointments')
        .where('patient_id', '==', patient_id)
        .stream()
    ]
#function to get all appointments with patient details
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

#function to update an appointment's information
def update_appointment(appointment_id, data):
    db.collection('appointments').document(appointment_id).update(data)

#function to delete an appointment
def delete_appointment(appointment_id):
    db.collection('appointments').document(appointment_id).delete()

#function to get a single appointment by id
def get_appointment(appointment_id):
    doc = db.collection("appointments").document(appointment_id).get()
    if doc.exists:
        return doc.to_dict() | {"id": doc.id}
    return None

#function to delete a patient by id
def delete_patient(patient_id):
    db.collection('patients').document(patient_id).delete()