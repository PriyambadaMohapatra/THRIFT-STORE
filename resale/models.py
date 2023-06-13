from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=300, default="")
    phone = models.CharField(max_length=111, default="")
    image = models.ImageField(upload_to="resale/images", default="")
    user_name = models.CharField(max_length=300, default="")
    size = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.product_name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

    def __str__(self):
        return self.name


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."


class Pay(models.Model):
    name = models.CharField(max_length=90)
    card = models.IntegerField()
    expiry = models.DateField()
    cvv = models.IntegerField()

    def __str__(self):
        return self.name
