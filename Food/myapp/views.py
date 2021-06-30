from django.shortcuts import render,redirect, HttpResponseRedirect
from django.http import HttpResponse
from .models import * 
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
class restraunt(View):
    def get(self, request):
        restraunt_list = Restraunt.objects.all()
        print("You are : ", request.session.get('customer'))
        return render(request, 'myapp/index.html', {'restraunt_list':restraunt_list})

class Detail(View):
    def get(self, request, id):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        print("Cart is", request.session['cart'] )
        print("Id", id)

        item_list = Item.objects.filter(restraunt_id=id)

        print(item_list)
        
        return render(request, 'myapp/detail.html',{'item_list':item_list})

    def post(self,request,id):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity :
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] =  1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart

        print("Cart is", request.session['cart'] )
        print('Cart Keys ', request.session['cart'].keys )

        item_list = Item.objects.filter(restraunt_id=id)
        return render(request, 'myapp/detail.html',{'item_list':item_list})

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        items = Item.get_items_by_id(ids)
        print("Cart products are", items)
        return render(request, 'myapp/cart.html', {'items': items})        

class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        items = Item.get_items_by_id(list(cart.keys()))
        print(address, phone, customer, cart, items)

        for item in items:
            print("Quantity",cart.get(str(item.id)))
            order = Order(
                customer = Customer(id = customer),
                item = item,
                price = item.item_price,
                address = address,
                phone = phone,
                quantity = cart.get(str(item.id)),
            )
            order.save()
            request.session['cart'] = {}
        return redirect('/cart')

class Orders(View):

    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        orders = orders.reverse()
        return render(request, 'myapp/orders.html', {'orders':orders})

class Signin(View):
    def get(self, request):
        return render(request, 'myapp/signin.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        error_message = None

        if not first_name:
            error_message = "First name Required !!!"

        elif not last_name:
            error_message = "Last name Required !!!"

        elif not phone:
            error_message = "Phone Number Required !!!"

        elif not email:
            error_message = "Email Required !!!"

        elif not (password1 == password2):
            error_message = "Password Doesn't Match !!!"

        elif not len(password1) > 8 :
            error_message = "Password Length must be of 8 character"

        

        customer = Customer(
            first_name= first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password = password1
        )

        if customer.isExists():
            error_message = "Username Exsits. Try another one."


        if not error_message:
            customer.password = make_password(customer.password)
            print(customer.password)
            customer.save()
            return redirect("/login")

        else:    
            return render(request, 'myapp/signin.html', {'error' : error_message, 'values': value})

class Login(View):

    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'myapp/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)

            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('/')
            else:
                error_message = "Email or Password Invaild !!!"
        else:
            error_message = "Email or Password Invaild !!!"
        print(email, password)
        return render(request, 'myapp/login.html', {'error':error_message})

class Logout(View):
    def get(self, request):
        request.session.clear()
        return redirect('/login')