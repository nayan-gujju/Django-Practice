from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView
from django.http import Http404
# Create your views here.

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