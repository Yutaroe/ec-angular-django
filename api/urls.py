from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'user'

router = DefaultRouter()
router.register('user',views.UserVieSet)
router.register('coffee',views.CoffeeVieSet)
router.register('topping', views.ToppingVieSet)
router.register('cart', views.CartVieSet)
router.register('ordercoffee', views.OrderCoffeeVieSet)


urlpatterns = [
    path('',include(router.urls))
]