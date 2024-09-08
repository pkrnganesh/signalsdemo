from django.db import models,transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
import time
import threading

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, created, **kwargs):
    if created:
        print(f"Signal handler started for: {instance.name}")
        time.sleep(3)  # Simulate a time-consuming operation
        print(f"Signal handler finished for: {instance.name}")



@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, created, **kwargs):
    if created:
        current_thread = threading.current_thread()
        print(f"Signal handler started for: {instance.name}")
        print(f"Signal handler thread: {current_thread.name} (ID: {current_thread.ident})")
        time.sleep(2)  # Simulate some work
        print(f"Signal handler finished for: {instance.name}")



class TransactionModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=TransactionModel)
def transaction_signal_handler(sender, instance, created, **kwargs):
    print(f"Signal received for: {instance.name}")
    # Modifying the instance within the signal handler
    instance.name = f"Modified_{instance.name}"
    # instance.save()  # This save won't trigger the signal again due to Django's built-in protection against recursive signals