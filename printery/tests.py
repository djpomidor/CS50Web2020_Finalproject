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

    def test_user(self):
        """Check that user is successfuly created."""
        user = User.objects.get(username="User1")
        self.assertTrue(user)

    def test_order(self):
        """Check that order is successfuly created"""
        order2 = Order.objects.get(name="Some name 2")
        self.assertTrue(order2)
