from django.test import TestCase
from .models import *

# Create your tests here.

class OrderTestCase(TestCase):

    def setUp (self):
        #Create users.
        user1 = User.objects.create(username = "User1", password = "12345678", email = "test1@test.com")
        user2 = User.objects.create(username = "User2", password = "12345678", email = "test2@test.com")

        #Create order.
        order1 = Order.objects.create(number = 1, name="Some name 1")
        order2 = Order.objects.create(number = 2, name="Some name 2")

        #create printing
        printing_object1 = Printing.objects.create()

    def test_user(self):
        """Check that user is successfuly created."""
        user = User.objects.get(username="User1")
        self.assertTrue(user)

    def test_order(self):
        """Check that order is successfuly created"""
        order2 = Order.objects.get(name="Some name 2")
        print("!!!!!", order2.id)
        self.assertTrue(order2)

    # def test_printing(self):
    #     """Check that printing is successfuly created"""
    #     printing_object = Printing.objects.get(order = 1)
    #     self.assertTrue(printing_object)
