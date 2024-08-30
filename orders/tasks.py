from celery import shared_task
from django.core.mail import send_mail
from .models import Order
from django.conf import settings

@shared_task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    try:
        # Retrieve the order object
        order = Order.objects.get(id=order_id)
        
        # Prepare the email details
        subject = f'Order nr. {order.id}'
        message = (
            f'Dear {order.first_name},\n\n'
            f'You have successfully placed an order.\n'
            f'Your order ID is {order.id}.'
        )
        
        # Send the email
        mail_sent = send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [order.email]
        )
        
        return mail_sent
    except Order.DoesNotExist:
        # Handle the case where the order does not exist
        return f'Order with id {order_id} does not exist.'
