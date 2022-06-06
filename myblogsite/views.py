from django.shortcuts import render

from blog.models import Blog


def base(request):
	blog = Blog.objects.all()

	return render(request,"base.html",{'blog_list':blog})