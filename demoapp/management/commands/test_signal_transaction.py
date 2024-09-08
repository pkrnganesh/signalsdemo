from django.core.management.base import BaseCommand
from demoapp.models import TransactionModel
from django.db import transaction

class Command(BaseCommand):
    help = 'Demonstrate signals running in the same database transaction as the caller'

    def handle(self, *args, **options):
        # Creating an instance of TransactionModel
        obj = TransactionModel.objects.create(name="Original")
        print(f"Name after first create: {obj.name}")

        # Starting a new transaction explicitly
        with transaction.atomic():
            # Updating the object within the transaction
            obj.name = "Updated"
            obj.save()
            print(f"Name inside transaction after save: {obj.name}")

            # Force a database refresh to ensure we're seeing the latest data
            obj.refresh_from_db()
            print(f"Name inside transaction after refresh: {obj.name}")

        # Force a database refresh outside the transaction
        obj.refresh_from_db()
        print(f"Name outside transaction after refresh: {obj.name}")

        # Demonstrating rollback
        try:
            with transaction.atomic():
                obj.name = "Will be rolled back"
                obj.save()
                print(f"Name inside transaction before error: {obj.name}")
                raise Exception("Simulating an error to cause rollback")
        except Exception as e:
            print(f"Caught exception: {e}")

        obj.refresh_from_db()
        print(f"Name after failed transaction: {obj.name}")