from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'admin'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
    )
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='studentprofile')
    date_of_birth = models.DateField()
    college_name = models.CharField(max_length=255)
    program = models.CharField(max_length=255)
    year_of_study = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username}'s Profile"

class ScholarshipApplication(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    application_form = models.FileField(upload_to='documents/application_form/', blank=True, null=True)
    passport_photographs = models.FileField(upload_to='documents/passport_photographs/', blank=True, null=True)
    identity_proof = models.FileField(upload_to='documents/identity_proof/', blank=True, null=True)
    address_proof = models.FileField(upload_to='documents/address_proof/', blank=True, null=True)
    class_10_marksheet = models.FileField(upload_to='documents/class_10_marksheet/', blank=True, null=True)
    class_12_marksheet = models.FileField(upload_to='documents/class_12_marksheet/', blank=True, null=True)
    income_certificate = models.FileField(upload_to='documents/income_certificate/', blank=True, null=True)
    caste_certificate = models.FileField(upload_to='documents/caste_certificate/', blank=True, null=True)
    domicile_certificate = models.FileField(upload_to='documents/domicile_certificate/', blank=True, null=True)
    bank_account_details = models.FileField(upload_to='documents/bank_account_details/', blank=True, null=True)
    bonafide_certificate = models.FileField(upload_to='documents/bonafide_certificate/', blank=True, null=True)
    fee_receipts = models.FileField(upload_to='documents/fee_receipts/', blank=True, null=True)
    proof_of_admission = models.FileField(upload_to='documents/proof_of_admission/', blank=True, null=True)
    academic_transcripts = models.FileField(upload_to='documents/academic_transcripts/', blank=True, null=True)
    disability_certificate = models.FileField(upload_to='documents/disability_certificate/', blank=True, null=True)
    passport_for_international = models.FileField(upload_to='documents/passport/', blank=True, null=True)
    document_status = models.CharField(max_length=20, default='pending')
    date_submitted = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    DOCUMENT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected'),
    )
    def __str__(self):
        return f"Application {self.id} by {self.student.user.username}"
