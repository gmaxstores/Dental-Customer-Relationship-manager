from django.shortcuts import render, redirect
from .firestore import (
    delete_patient,
    get_all_appointments,
    delete_appointment,
    get_appointment,
    get_patients,
    update_appointment,
    get_patient,
    create_patient,
    create_appointment,
    get_appointments_for_patient
)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .permissions import is_admin, is_receptionist

# view for the dashboard
@login_required
def dashboard(request):
    patients = get_patients()
    appointments = get_all_appointments()
    return render(request, "hello/dashboard.html", {
        'patients_count': len(patients),
        'upcoming_appointments': appointments
    })


#view for listing patients
@login_required
def patient_list(request):
    patients = get_patients()
    return render(request, 'hello/patient_list.html', {
        'patients': patients
    })


#view for creating a new patient
#Route protected to only allow admin and receptionist roles
@login_required
def patient_create(request):
    if not (is_admin(request.user) or is_receptionist(request.user)):
        return HttpResponseForbidden("Access denied")
    if request.method == 'POST':
        create_patient({
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'phone': request.POST['phone'],
            'email': request.POST.get('email')
        })
        return redirect('patient_list')


    return render(request, 'hello/patient_form.html')


#view for patient details
@login_required
def patient_detail(request, patient_id):
    patient = get_patient(patient_id)
    appointments = get_appointments_for_patient(patient_id)


    return render(request, 'hello/patient_detail.html', {
        'patient': patient,
        'appointments': appointments
    })


#view for creating an appointment for a patient
#Route protected to allow only receptionist role
@login_required
def appointment_create(request, patient_id):
    if not (is_receptionist(request.user)):
        return HttpResponseForbidden("Only the receptionist can create appointments.")
    if request.method == 'POST':
        create_appointment({
            'patient_id': patient_id,
            'dentist': request.POST['dentist'],
            'date': request.POST['date'],
            'status': 'scheduled'
        })
        return redirect('patient_detail', patient_id=patient_id)


    return render(request, 'hello/appointment_form.html', {
        'patient_id': patient_id
    })

#view for editing an appointment
#Route protected to allow only receptionist role
@login_required
def edit_appointment(request, appointment_id):
    if not (is_receptionist(request.user)):
        return HttpResponseForbidden("Only the receptionist can edit appointments.")
    appointment = get_appointment(appointment_id)
    if not appointment:
        return redirect("dashboard")
    if request.method == 'POST':
        # Logic to edit the appointment
        update_appointment(appointment_id, {
            'dentist': request.POST['dentist'],
            'date': request.POST['date'],
            'status': request.POST['status']
        })
        return redirect('patient_detail', patient_id=appointment['patient_id'])
    return render(request, 'hello/appointment_edit.html', {
        'appointment': appointment
    })

#view for deleting an appointment
##Route protected to allow only receptionist role and admin role
@login_required
def delete_appointment_view(request, appointment_id):
    if not (is_admin(request.user) or is_receptionist(request.user)):
        return HttpResponseForbidden("Only admins can delete appointments")
    appointment = get_appointment(appointment_id)

    if not appointment:
        return redirect("dashboard")

    if request.method == "POST":
        delete_appointment(appointment_id)
        return redirect(
            "patient_detail",
            patient_id=appointment["patient_id"]
        )

    return render(request, "hello/appointment_delete.html", {
        "appointment": appointment
    })

#view for deleting a patient
#route protected to allow only admin role
@login_required
def patient_delete(request, patient_id):
    if not (is_admin(request.user)):
        return HttpResponseForbidden("Only admins can delete patients")
    patient = get_patient(patient_id)

    if not patient:
        return redirect("dashboard")

    if request.method == "POST":
        delete_patient(patient_id)
        return redirect("patient_list")

    return render(request, "hello/patient_delete.html", {
        "patient": patient
    })