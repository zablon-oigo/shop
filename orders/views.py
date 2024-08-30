from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from .models import OrderItem,Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.contrib.admin.views.decorators import staff_member_required
import weasyprint
from django.template.loader import render_to_string
from django.http import HttpResponse

 
def order_create(request):
    cart=Cart(request)
    if request.method == 'POST':
        form=OrderCreateForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'], quantity=item['quantity'] )
            
            # clear the cart
            cart.clear()
            order_created.delay(order.id)
            request.session['order_id']=order.id

            return redirect(reverse('payment:process'))
    else:
        form=OrderCreateForm()
    return render(request,'orders/create.html',{'cart':cart,'form':form})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/detail.html', {'order': order})

@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="order_{}.pdf"'.format(order.id)
    weasyprint.HTML(string=html).write_pdf(response, )
    return response