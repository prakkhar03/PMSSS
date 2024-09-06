from django.core.mail import send_mail
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import ScholarshipApplication
from .serializers import ScholarshipApplicationSerializer
import datetime

class ScholarshipApplicationViewSet(viewsets.ModelViewSet):
    queryset = ScholarshipApplication.objects.all()
    serializer_class = ScholarshipApplicationSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        student_email = request.user.email  
        application_id = serializer.data['id']
        self.send_application_email(student_email, application_id, 'submitted')

        return Response({
            'status': 'success',
            'message': 'Application submitted successfully with documents',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

    def send_application_email(self, recipient_email, application_id, status_type):
        subject = f'Scholarship Application {status_type.capitalize()}'
        message = f'Your scholarship application with ID {application_id} has been {status_type}.'
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient_email],
            fail_silently=False,
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        student_email = request.user.email
        application_id = serializer.data['id']
        self.send_application_email(student_email, application_id, 'updated')

        return Response({
            'status': 'success',
            'message': 'Application updated successfully with documents',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        student_email = request.user.email
        subject = 'Scholarship Application Deleted'
        message = f'Your scholarship application with ID {instance.id} has been deleted.'
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [student_email],
            fail_silently=False,
        )

        return Response({
            'status': 'success',
            'message': 'Application deleted successfully',
        }, status=status.HTTP_204_NO_CONTENT)

    def verify(self, request, pk=None):
        try:
            application = self.get_object()
            application.is_verified = True
            application.verification_date = datetime.now() 
            application.save()

            student_email = application.student.email
            self.send_application_email(student_email, application.id, 'verified')

            return Response({
                'status': 'success',
                'message': 'Application verified successfully',
                'data': ScholarshipApplicationSerializer(application).data
            }, status=status.HTTP_200_OK)
        except ScholarshipApplication.DoesNotExist:
            return Response({'error': 'Application not found'}, status=status.HTTP_404_NOT_FOUND)

    def submit(self, request, pk=None):
        try:
            application = self.get_object()
            if not application.is_verified:
                return Response({'error': 'Application must be verified before submission'}, status=status.HTTP_400_BAD_REQUEST)

            application.is_submitted = True
            application.submission_date = datetime.now()  
            application.save()

            student_email = application.student.email
            self.send_application_email(student_email, application.id, 'submitted')

            return Response({
                'status': 'success',
                'message': 'Application submitted successfully',
                'data': ScholarshipApplicationSerializer(application).data
            }, status=status.HTTP_200_OK)
        except ScholarshipApplication.DoesNotExist:
            return Response({'error': 'Application not found'}, status=status.HTTP_404_NOT_FOUND)
