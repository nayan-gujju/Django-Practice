from django.shortcuts import render
from django.views.generic.base import RedirectView, TemplateView
# Create your views here.

class YouTubeView(RedirectView):
    url = 'https://www.youtube.com'

class YouView(RedirectView):
    pattern_name = 'mindex'
    permanent = True
    query_string = True
    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        return super().get_redirect_url(*args, **kwargs)