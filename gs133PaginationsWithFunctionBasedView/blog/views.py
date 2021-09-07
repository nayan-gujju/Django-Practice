from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator
# Create your views here.

def post_list(request):
    all_posts = Post.objects.all().order_by('id')
    paginator = Paginator(all_posts, 2, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(all_posts)
    print('+++++++++++++++++++++++')
    print(paginator)
    print('+++++++++++++++++++++++')
    print(page_number)  
    print('+++++++++++++++++++++++')
    print(page_obj)
    return render(request, 'blog/index.html',{'all':page_obj})