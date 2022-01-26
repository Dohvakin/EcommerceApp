from django.shortcuts import render, redirect
from seller.models import Products
from EcommerceApp.models import UserProfile
from seller.models import Products
from buyer.models import Cart
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.

@login_required
def home(request):
	count = Cart.objects.filter(user_profile__user_id=request.user).count()
	return render(request, 'welcomeBuyer.html', {'count' : count})







@login_required
def products(request):
	p_all = Products.objects.all()
	count = Cart.objects.filter(user_profile__user_id=request.user).count()
	return render(request, 'products.html', {'products' : p_all, 'count' : count})






@login_required
def cart(request, id):
	user = UserProfile.objects.get(user__username=request.user)
	pid = Products.objects.get(id=id)
	url = '/buyer/products/'
	try:
		c = Cart(user_profile=user, product=pid)
		c.save()
	except:
		return HttpResponse('<script>alert("Product is already added in your cart");\
             window.location="%s"</script>'%url)
	
	return HttpResponse('<script>alert("Product has been added in the Cart");\
             window.location="%s"</script>'%url)




@login_required
def cartvalue(request):
	count = Cart.objects.filter(user_profile__user_id=request.user).count()

	user = UserProfile.objects.get(user__username=request.user)
	p = Cart.objects.filter(user_profile_id=user.id)
	items = []
	for i in p:
		items.append(Products.objects.get(id=i.product_id))

	return render(request, 'cartdetails.html', {'added_products' : items, 'count' : count})




def cartcalculate(request):
	if request.method == 'POST':
		
		#getting data from form with quantity etc
		q = request.POST.getlist('productqty')
		pid = request.POST.getlist('pid')
		price = request.POST.getlist('price')
		sum = 0
		for i in range(len(q)):
			sum = sum + int(q[i])*float(price[i])

			#Update product stock
			updateProduct = Products.objects.filter(id=pid[i])
			updatedQty = updateProduct[0].product_avail-int(q[i])
			updateProduct.update(product_avail=updatedQty)

		#Deleting cart value after checkout
		cartObjs = Cart.objects.filter(user_profile__user_id=request.user)
		cartObjs.delete()

		count = Cart.objects.filter(user_profile__user_id=request.user).count()

		message = 'Your order is processed of {}'.format(sum)
		send_mail('Order details', message, 'XXXXX', ['XXXXXX'])
		return render(request, 'checkout.html', {'data' : sum, 'count' : count})