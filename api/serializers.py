from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Coffee, Topping, Carts, OrderCoffee, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')
    
class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = ('id', 'coffee_name', 'coffee_detail', 'img', 'coffee_priceL', 'coffee_priceM')

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ('id', 'topping_name', 'topping_priceL', 'topping_priceM')

class CartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carts
        fields = ('id','userCart','order_name', 'addressnumber', 'address', 'email', 'order_date', 'order_time', 'tel', 'status')
        # extra_kwargs = {'userCart': {'read_only': True}}

class OrderCoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCoffee
        fields = ('id', 'item_number','coffee_id', 'item_size', 'toppings', 'carts')
