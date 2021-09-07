from django.http import HttpResponse

class BrotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('one time brother middleware configrations')
    
    def __call__(self, request):
        print('this is brother before view')
        response = self.get_response(request)
        print('this is brother after view')
        return response

class FatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('one time father middleware configrations')
    
    def __call__(self, request):
        print('this is father before view')
        #return HttpResponse('nonononononononoon')        
        response = self.get_response(request)
        print('this is father after view')
        return response

class MotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('one time mother middleware configrations')
    
    def __call__(self, request):
        print('this is mother before view')
        response = self.get_response(request)
        print('this is mother after view')
        return response
