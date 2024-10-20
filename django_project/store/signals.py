from django.db.models.signals import pre_save
from django.dispatch import receiver
from store.models import Product


@receiver(pre_save,sender=Product)
def prodact_save_handler(sender,**kwargs):
    print('signal works')