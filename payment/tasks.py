from io import BytesIO  
from celery import shared_task
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
import weasyprint
from orders.models import Order

@shared_task
def payment_completed(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)

    # create invoice e-mail
    subject = f'Mini mart - Invoice no. {order.id}'
    message = 'Please, find attached the invoice for your recent purchase.'
    email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [order.email])
    
    # generate PDF
    html = render_to_string('orders/pdf.html', {'order': order})
    out = BytesIO() 
    weasyprint.HTML(string=html).write_pdf(out)
    
    # attach PDF file
    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')
    
    # send e-mail
    email.send()
