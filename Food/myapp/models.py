from django.db import models
import datetime

# Create your models here.      
class Restraunt(models.Model):
    def __str__(self):
        return '%s %s' % (self.name, self.branch)

    restraunt_image= models.ImageField(default='default.jpg', upload_to='restraunt_images/')
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
 
class Item(models.Model):
    def __str__(self):
        return self.item_name
    

    FOOD_TYPE = (
        ('Veg' , "Veg"),
        ('Non-Veg' , 'Non-Veg'),
    )
    
    id = models.AutoField(primary_key=True)
    restraunt = models.ForeignKey(Restraunt, on_delete=models.CASCADE, null=True)
    item_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, null=True)
    item_price = models.IntegerField(max_length=50)
    food_type = models.CharField(max_length=10, choices=FOOD_TYPE)
    item_image= models.ImageField(default='default.jpg', upload_to='item_images/')

    @staticmethod
    def get_items_by_id(ids):
        return Item.objects.filter(id__in = ids)

class Customer(models.Model):
    def __str__(self):
        return self.first_name

    id = models.AutoField(primary_key=True)
    first_name= models.CharField(max_length=100)            
    last_name= models.CharField(max_length=100)
    phone= models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
  
class Order(models.Model):

    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=1000, null= True)
    phone = models.CharField(max_length=10, null=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order\
            .objects\
            .filter(customer = customer_id)\
            .order_by('-date')