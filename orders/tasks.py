from celery import shared_task
from django.core.mail import EmailMessage
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
        subject = f'Order Confirmation: {order.id}'
        html_message = f"""
        <html>
        <body style="font-family: Arial, sans-serif; color: #333; margin: 0; padding: 0; background-color: #f4f4f4;">
            <div style="max-width: 600px; margin: 20px auto; background: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
                <h1 style="color: #007bff; font-weight: 600; font-size: 24px; margin-bottom: 20px;">Thank You for Your Order!</h1>
                <p style="color: #4a4a4a; font-size: 16px; line-height: 1.6;">Dear {order.first_name},</p>
                <p style="color: #4a4a4a; font-size: 16px; line-height: 1.6;">You have successfully placed an order.</p>
                <p style="color: #4a4a4a; font-size: 16px; line-height: 1.6;">Your order ID is <strong>{order.id}</strong>.</p>
                <p style="color: #4a4a4a; font-size: 16px; line-height: 1.6;">We will process your order as soon as possible and notify you once it’s shipped.</p>
                <p style="text-align: center;">
                    <a href="" style="display: inline-block; padding: 10px 20px; font-size: 16px; color: #ffffff; background-color: #007bff; text-decoration: none; border-radius: 5px; text-align: center;">Track Your Order</a>
                </p>
                <div style="color: #4a4a4a; font-size: 14px; text-align: center; margin-top: 20px;">
                    <p>Thank you for shopping with us!</p>
                    <p>Best Regards,<br>Online Shop</p>
                </div>
            </div>
        </body>
        </html>
        """

        # Create the email
        email = EmailMessage(
            subject=subject,
            body=html_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[order.email]
        )
        email.content_subtype = 'html'

        # Send the email
        mail_sent = email.send()

        return mail_sent
    except Order.DoesNotExist:
        # Handle the case where the order does not exist
        return f'Order with id {order_id} does not exist.'
