from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.http import Http404
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['id']
    paginate_by = 2
    paginate_orphans = 1

    """ def get_context_data(self, *args,**kwargs):
        try:
            return super(PostListView, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(PostListView, self).get_context_data(*args, **kwargs) """

    def paginate_queryset(self, QuerySet, page_size):
        try:
            return super().paginate_queryset(QuerySet, page_size)
        except Http404:
            self.kwargs['page'] = 1
            return super().paginate_queryset(QuerySet, page_size)

    


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/next.html'


decorators = [login_required, staff_member_required]
@method_decorator(decorators, name='dispatch')
class AddCreateView(CreateView):
    model = Post
    template_name = 'blog/home.html'
    success_url = '/'
    fields = ('title', 'description', 'writtername')

    


    