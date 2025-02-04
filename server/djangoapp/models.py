from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    # - Name
    name = models.CharField(null=False, max_length=100)
    # - Description
    description = models.CharField(null=True, max_length=250)
    # - Any other fields you would like to include in car make model
    # - __str__ method to print a car make object
    def __str__(self):
        return self.name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    # - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
    make = models.ForeignKey('CarMake', on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=50, default='SampleModel')
    CAR_CHOICES = (
    ("SEDAN", "Sedan"),
    ("SUV", "SUV"),
    ("TRUCK", "Truck"),
    ("CONVERTIBLE", "Convertible"),
    ("VAN", "Van"),
    )
    car = models.CharField(max_length=11, choices=CAR_CHOICES, default="SEDAN")
    dealerid = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return f'{self.name},{self.make},{self.year}'


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        self.address = address
        self.city = city
        self.full_name = full_name
        self.id = id
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.st = st
        self.zip = zip

    def __str__(self):
        return f"Dealer ID: {self.id}, Name: {self.full_name}, City: {self.city}, Address: {self.address}, Zip: {self.zip}, State: {self.st}"



# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, id, sentiment=None):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment
        self.id = id
