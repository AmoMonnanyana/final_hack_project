from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, customerOrderHistory

#@receiver(post_save, sender=Order)
#def update_order_status(sender, instance, **kwargs):
#    """
#    Signal handler to update order status instantly when changed.
#    """
#    order_list_status = instance.order_status
#    if order_list_status == 'shipped' or order_list_status == 'delivered':
#        # Update the related customerOrderHistory instance
#        customer_history = customerOrderHistory.objects.get(order_number_on_orderlist=instance)
#        customer_history.customer_order_status = order_list_status
#        customer_history.save()