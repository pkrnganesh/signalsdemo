import threading
from django.core.management.base import BaseCommand
from demoapp.models import MyModel

class Command(BaseCommand):
    help = 'Demonstrate that signals run in the same thread as the caller'

    def handle(self, *args, **options):
        current_thread = threading.current_thread()
        print(f"Main thread: {current_thread.name} (ID: {current_thread.ident})")

        print("Creating first object...")
        obj1 = MyModel.objects.create(name="First")
        print("First object created")

        print("Creating second object...")
        obj2 = MyModel.objects.create(name="Second")
        print("Second object created")

        print(f"Finished in main thread: {current_thread.name} (ID: {current_thread.ident})")