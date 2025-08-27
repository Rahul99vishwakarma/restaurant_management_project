from django.conf import setting
def restaurant_name(request):
    return{
        'restaurant_name':getattr(setting'restaurant_name','my restaurant')
    }