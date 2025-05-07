from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Orders(models.Model):
    order_number = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    
    def __str__(self):
        """
        `self.customer.name` could issue N+1 query if we do not fetch orders using `select_related('customer')`.
        so instead, we can use `self.customer.customer_id` cause `customer_id` is available by default, 
        don't require any query. Since `customer_id` loses readability, we don't use it usually
        """
        return f'Order {self.order_number} by {self.customer.name}' 
