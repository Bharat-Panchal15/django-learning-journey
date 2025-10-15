from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order

@receiver(post_save, sender=Order)
def reduce_stock(sender,instance,created,**kwargs):
    if created:
        product = instance.product
        product.stock -= instance.quantity
        product.save()