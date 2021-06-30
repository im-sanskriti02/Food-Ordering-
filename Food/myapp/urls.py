from django.urls import path
from .views import *
from Food import settings
from django.conf.urls.static import static
from .middlewares.auth import auth_middleware

app_name = 'myapp'
urlpatterns = [
    path('', restraunt.as_view(), name="index"),
    path('detail/<int:id>/', Detail.as_view(), name="detail"),
    path('cart/', Cart.as_view(), name="cart"),
    path('signin/', Signin.as_view(), name="signin"),
    path('check-out/', Checkout.as_view(), name="checkout"),
    path('orders/', auth_middleware(Orders.as_view()), name="orders"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)