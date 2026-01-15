from django.db import models
from django.contrib.auth.models import User

# Model to extend the User model with staff roles
class StaffProfile(models.Model):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("dentist", "Dentist"),
        ("receptionist", "Receptionist"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.role})"
