from django.contrib.auth.models import User, auth
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from blog.forms import ContactForm, CreateBlogForm, LoginForm, SignupForm, UpdateBlogForm
from django.contrib.auth.hashers import check_password
from blog.models import Blog, Category, Contact

# Create your views here.
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():

			uname = request.POST['uname']
			email = request.POST['email']
			mobno = request.POST['mobno']
			udisc = request.POST['udisc']


			user = Contact(uname=uname,email=email,mobno=mobno,udesc= udisc)
			user.save()

			return redirect('blog:home')

	else:
		form = ContactForm()
	return render(request, 'blog/contact.html', {'form': form})
def home(request):
	cat_list = Category.objects.all()

	return render(request,"blog/home.html",{"Category_list":cat_list})

def login(request):
	if request.method== 'POST':

		form = LoginForm(request.POST)

		if form.is_valid():
			cd = form.cleaned_data

			username = cd['username']
			password = cd['password']

			user = get_object_or_404(User, username=username)

			auth.login(request,user)
			return redirect("users:home")

	else:
		form = LoginForm()
	return render(request,'blog/home.html', {'form':form})




def register(request):

	if request.method == 'POST':

		form = SignupForm(request.POST)

		if form.is_valid():
			cd = form.cleaned_data
			# print(cd['first_name'])

			# #first_name = form.cleaned_data['first_name']
			# last_name = cd['last_name']
			# username = cd['username']
			# password1 = cd['password1']
			# password2 = cd['password2']
			# email = cd['email']

			first_name = request.POST['first_name']
			last_name = request.POST['last_name']
			username = request.POST['username']
			password1 = request.POST['password1']
			password2 = request.POST['password2']
			email = request.POST['email']


			user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)

			return redirect('users:login')

	else:
		form = SignupForm()
	return render(request, 'blog/home.html', {'regform': form})

def logout(request):
	auth.logout(request)
	return redirect('users:home') 

def show_blog(request, id):
	category = get_object_or_404(Category, pk=id)
	blog = category.blog_set.all()

	return render(request, 'blog/show.html', {'blog_list':blog,'cat':category})

def add_blog(request,id, pk):
	if request.method == 'POST':
		form  = CreateBlogForm(request.POST)

		if form.is_valid():
			cd = form.cleaned_data
			title = cd['title']
			discription = cd['discription']
			regdate = cd['regdate']

			cat = get_object_or_404(Category,id)
			cnm = cat.cname
			author =  get_object_or_404(User, pk = pk)

			new_blog = author.blog_set.create(cname =cnm,title=title,discription=discription,regdate=regdate)
			new_blog.save()

			return redirect('users:blog')
		

	else:
		form = CreateBlogForm()

	return render(request, 'blog/addblog.html', {'form':form})


def delete_blog(request,id,id1):
	blog = get_object_or_404(Blog, pk =id1)	
	blog.delete()
	return redirect('blog:home')

def update_blog(request,id ,id1):
	blog = get_object_or_404(Blog, pk = id1)
	data = {'title': blog.title, 'discription':blog.discrption, 'regdate':blog.regdate}

	if request.method == 'POST':
		form = UpdateBlogForm(request.POST)

		if form.is_valid():
			cd = form.cleaned_data
			title = cd['title']
			discription = cd['discription']
			regdate = cd['regdate']

			blog.title = title
			blog.discrption = discription
			blog.regdate = regdate
			blog.save()

			return redirect('blog:home')

	else:
		form = UpdateBlogForm(data)
		if form.is_bound :
			return render(request, 'blog/update.html', {'form': form})
	return redirect('blog:home')