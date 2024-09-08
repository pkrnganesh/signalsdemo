from django.core.management.base import BaseCommand
from demoapp.models import MyModel
import time

class Command(BaseCommand):
    help = 'Demonstrate synchronous signal execution'

    def handle(self, *args, **options):
        start_time = time.time()
        
        print("Creating first object...")
        obj1 = MyModel.objects.create(name="First")
        print("First object created")
        
        print("Creating second object...")
        obj2 = MyModel.objects.create(name="Second")
        print("Second object created")
        
        end_time = time.time()
        print(f"Total execution time: {end_time - start_time:.2f} seconds")
