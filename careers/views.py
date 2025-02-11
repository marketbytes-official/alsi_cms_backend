from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .models import CareersForm,CareersBanner
from .serializers import CareersFormSerializer,CareersBannerSerializer
from django.core.files.storage import default_storage
from django.utils.html import escape

class CareersFormViewSet(viewsets.ModelViewSet):
    queryset = CareersForm.objects.all()
    serializer_class = CareersFormSerializer
    permission_classes = [AllowAny]

class CareersBannerViewSet(viewsets.ModelViewSet):
    queryset = CareersBanner.objects.all()
    serializer_class = CareersBannerSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            form_data = request.data

            # Subject and message
            subject = f"New Career Application from {escape(form_data['name'])}"
            resume_url = None

            # Save file temporarily if attached
            if 'resume' in request.FILES:
                resume = request.FILES['resume']
                resume_path = default_storage.save(f"resumes/{resume.name}", resume)
                resume_url = default_storage.url(resume_path)

            html_message = render_to_string('emails/career_form.html', {
                'name': form_data.get('name', 'N/A'),
                'email': form_data.get('email', 'N/A'),
                'phone': form_data.get('phone_number', 'N/A'),
                'message': form_data.get('message', 'N/A'),
                'attachment_url': resume_url,
            })

            # Sending email
            to_email = settings.EMAIL_HOST_USER
            email = EmailMessage(
                subject=subject,
                body=html_message,
                from_email=settings.EMAIL_HOST_USER,
                to=[to_email],
            )
            email.content_subtype = "html"

            if 'resume' in request.FILES:
                email.attach(resume.name, resume.read(), resume.content_type)

            try:
                email.send()
                print("Email sent successfully.")
            except Exception as email_error:
                print(f"Failed to send email: {str(email_error)}")
                return Response({'error': 'Failed to send email'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return response
        except Exception as e:
            print(f"Error creating career application: {str(e)}")
            return Response({'error': 'Failed to submit the application'}, status=status.HTTP_400_BAD_REQUEST)


