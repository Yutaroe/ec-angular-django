from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from . import serializers
from .models import Coffee, Topping, Carts, OrderCoffee, User

class UserVieSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)

class CoffeeVieSet(viewsets.ModelViewSet):
    queryset = Coffee.objects.all()
    serializer_class = serializers.CoffeeSerializer
    permission_classes = (AllowAny,)


class ToppingVieSet(viewsets.ModelViewSet):
    queryset = Topping.objects.all()
    serializer_class = serializers.ToppingSerializer
    permission_classes = (AllowAny,)


class CartVieSet(viewsets.ModelViewSet):
    queryset =  Carts.objects.all()
    serializer_class = serializers.CartsSerializer 
    permission_classes = (AllowAny,)


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    # def get_queryset(self):
    #     queryset = Carts.objects.all()
    #     queryset = queryset.filter(user=self.request.user.id )
    #     return queryset

    

class MyCartListView(generics.ListAPIView):
    quaryset = Carts.objects.all()
    serializer_class = serializers.CartsSerializer
    permission_classes = (AllowAny,)


    def get_queryset(self):
        queryset = Carts.objects.all()
        queryset = queryset.filter(user=self.request.user )
        return queryset


class OrderCoffeeVieSet(viewsets.ModelViewSet):
    queryset = OrderCoffee.objects.all()    
    serializer_class = serializers.OrderCoffeeSerializer
    permission_classes = (AllowAny,)
