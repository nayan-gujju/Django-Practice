from django.urls import path,register_converter
from enroll import converters
from enroll import views
register_converter(converters.FourDigitConverter, 'yyyy')
urlpatterns = [
     path('student/<my_id>/', views.show_details,name='detail'),
    path('student/<yyyy:my_id>/<int:my_subid>/', views.show_subdetails,name='subdetail'),
]