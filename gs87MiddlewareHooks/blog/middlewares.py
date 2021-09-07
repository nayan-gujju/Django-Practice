from django.http import HttpResponse

class MyPorcessMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(request, *args, **kwargs):
        print('this process view - before view ')
        #return HttpResponse('This is before view')
        return None 

class MyExceptionMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        print('Exception occured')
        msg = exception
        class_name = exception.__class__.__name__
        print(class_name)
        return HttpResponse(msg)

class MyTemplateResponseMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        print('Process Template Response From Middleware')
        response.context_data['name'] = 'Gujarati'
        return response 