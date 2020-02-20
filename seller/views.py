from django.shortcuts import render, redirect
from seller.models import Products, Category
from EcommerceApp.models import UserProfile
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
	return render(request, 'welcomeSeller.html')

@login_required
def addproduct(request):
	p = Category.objects.all()

	if request.method == 'POST':
		pname = request.POST['pname']
		desc = request.POST['desc']
		price = request.POST['price']
		pic = request.FILES['pic']
		qty = request.POST['qty']
		catid = Category.objects.get(cat=request.POST['catid'])
		uname = request.POST['uname']

		pobj = Products(product_name=pname, product_desc=desc, product_price=price, added_by_seller=uname, product_img=pic, product_avail=qty, category=catid)
		pobj.save()
		return redirect('/seller/addproduct/')
	return render(request, 'addproduct.html', {'pform' : p})