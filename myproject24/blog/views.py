from django.shortcuts import render
from . models import Post
from django.db.models import Q
# Create your views here.
def post_list(request):
  query = request.GET.get('q') # serach keywords
  category = request.GET.get('category') # category filter
  posts = Post.objects.all()

# serach using Q object

  if query:
    posts = posts.filter(
      Q(title__icontains=query)|
      Q(content__icontains=query)
      )
    # filter bye category
  if category:
    posts = posts.filter(category__iexact=category)

  return render(request,'blog/post_list.html' ,{
    'posts':posts,
    'query':query,
    'category':category,
  })