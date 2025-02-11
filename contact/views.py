from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.mail import send_mail
from .models import ContactBanner, ContactForm
from .serializers import ContactBannerSerializer, ContactFormSerializer
from django.conf import settings
from django.template.loader import render_to_string

class ContactBannerViewSet(viewsets.ModelViewSet):
    queryset = ContactBanner.objects.all()
    serializer_class = ContactBannerSerializer
    permission_classes = [AllowAny]

class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            form_data = request.data

            subject = f"New Contact Form Submission from {form_data['name']}"

            html_message = render_to_string('emails/contact_form.html', {
                'name': form_data['name'],
                'email': form_data['email'],
                'phone': form_data['phone'],
                'message': form_data['message'],
            })

            message = f"Message from {form_data['name']} ({form_data['email']}, {form_data['phone']}):\n\n{form_data['message']}"

            to_email = settings.EMAIL_HOST_USER
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [to_email], html_message=html_message)
                print("Email sent successfully.")
            except Exception as email_error:
                print(f"Failed to send email: {str(email_error)}")
                return Response({'error': 'Failed to send email'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return response
        except Exception as e:
            print(f"Error creating form: {str(e)}")
            return Response({'error': 'Failed to submit the form'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        try:
            ContactForm.objects.all().delete()
            return Response({'status': 'All messages deleted successfully'}, status=200)
        except Exception as e:
            return Response({'status': f'Failed to delete messages: {str(e)}'}, status=500)

    def destroy(self, request, *args, **kwargs):
        try:
            contact_form = self.get_object()
            contact_form.delete()
            return Response({'status': 'Message deleted successfully'}, status=200)
        except Exception as e:
            return Response({'status': f'Failed to delete message: {str(e)}'}, status=500)
