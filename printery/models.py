from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.db.models import Max


# Create your models here.
class User(AbstractUser):
    # orders = models.ManyToManyField("Order", blank=True, symmetrical=False, related_name="order")
    phone_number = models.IntegerField(null=True, blank=True)
    company = models.ForeignKey('Company', null=True, blank=True, on_delete=models.CASCADE)
    is_customer = models.BooleanField(default=True)
    is_employee = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username}"

# class Employee(models.Model):
#     first_name = models.CharField(max_length=64)
#     middle_name = models.CharField(max_length=64)
#     last_name = models.CharField(max_length=64)
#     position = models.CharField(max_length=64)
#     phone_number = models.IntegerField()
#     email = models.CharField(max_length=64)
#     def __str__(self):
#         return f"{self.first_name}"

#########################################################################

class Company(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(blank=True, max_length=64)
    city = models.CharField(blank=True, max_length=25)
    postal_code = models.IntegerField(blank=True, null=True)
    country = models.CharField(blank=True, max_length=56)
    email = models.CharField(blank=True, max_length=64)
    phone = PhoneNumberField(null=False, blank=True)
    is_manufacturer = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    def __str__(self):
        return self.name

#########################################################################

class Paper(models.Model):
    name = models.CharField(max_length=64)
    TYPE_CHOICES = [
        ('GL', 'Glossy'),
        ('MAT', 'Matte'),
        ('OFF', 'Offset'),
    ]
    type = models.CharField(max_length=3,
        choices=TYPE_CHOICES,
        )
    class Density(models.IntegerChoices):
        D80 = 80, '80 gr/m2'
        D120 = 120, '120 gr/m2'
        D150 = 150, '150 gr/m2'
        D200 = 200, '200 gr/m2'
        D250 = 250, '250 gr/m2'
    density = models.IntegerField(choices=Density.choices)
    width = models.IntegerField()
    height = models.IntegerField()
    manufacturer = models.ManyToManyField(Company, blank=True, related_name="made_by")

    def __str__(self):
        return f"{self.name} {self.type} {self.density}"

###########################################################################

class Order(models.Model):
    def counter():
        no = Order.objects.aggregate(Max('number'))
        if no == None:
            return 1
        else:
            return no['number__max'] + 1

    number = models.IntegerField(unique=True, default=counter)
    name = models.CharField(blank=True, max_length=16)
    owner = models.ManyToManyField('User', blank=True, related_name="order_owners")

    BOOK = 'BK'
    CALENDAR = 'CL'
    MAGAZINE = 'MZ'
    NEWSPAPER = 'NP'
    FLYERS = 'FL'
    TYPE_CHOICES = [
        (None, ""),
        (BOOK, 'Book'),
        (CALENDAR, 'Calendar'),
        (MAGAZINE, 'Magazine'),
        (NEWSPAPER, 'Newspaper'),
        (FLYERS, 'Flyers')
    ]
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, blank=True)
    circulation = models.IntegerField(null=True, blank=True)

    BINDING_CHOICES = [
        (None, 'Select...'),
        ('GLU', 'Glue'),
        ('STA', 'Staple'),
        ('HAR', 'Hardcover'),
        ('FOL', 'Folding'),
    ]
    binding = models.CharField(blank=True, max_length=4, choices=BINDING_CHOICES,)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

#    def __str__(self):
#        return f"{self.number} {self.name}"

    def serialize(self):
        return {
            "number": self.number,
            "name": self.name,
            "owner": [user.last_name for user in self.owner.all()],
            "type": self.type,
            "circulation": self.circulation,
            "binding": self.binding,
            "width": self.width,
            "height": self.height,
            "created": self.created.strftime("%b %d %Y, %I:%M %p"),
        }


######################################################################################

class Part(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # NAME_CHOICES =[
    #     ('BLO', 'Block'),
    #     ('COV', 'Cover'),
    #     ('INS', 'Insert'),
    # ]
    part_name = models.CharField(blank=True, max_length=3)
    pages = models.IntegerField(null=True, blank=True)
    paper = models.ForeignKey(Paper, null=True, on_delete=models.CASCADE, related_name="paper", blank=True)
    COLOR_CHOICES = [
        ('4_4', '4+4'),
        ('4_0', '4+0'),

    ]
    color = models.CharField(blank=True, max_length=3, choices=COLOR_CHOICES)

    LAMINATE_CHOICES = [
        ('MAT', 'Matte'),
        ('GL', 'Glossy'),
    ]
    laminate = models.CharField(blank=True, max_length=3, choices=LAMINATE_CHOICES)

    uflak = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.part_name}"
