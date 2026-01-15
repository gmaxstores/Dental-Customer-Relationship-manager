#created to define permission checks based on user roles
def is_admin(user):
    return user.staffprofile.role == "admin"

def is_dentist(user):
    return user.staffprofile.role == "dentist"

def is_receptionist(user):
    return user.staffprofile.role == "receptionist"
