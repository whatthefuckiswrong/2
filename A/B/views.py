from django.views import View
from django.http import JsonResponse
import json
from .models  import Car
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')

class Soppingcart (View):
    def post(self,request):

        data = json.loads (request.body.decode("utf-8"))
        p_mane = data.get('product_name')
        p_price = data.get('product_price')
        p_quantity = data.get('product_quantity')

        product_data ={
            'priduct_name': p_mane,
            'prodict_price': p_price,
            'product_quantity': p_quantity,

          }
        Car_A = Car.objects.create (**product_data)

        data = {
            "massage":f"new item added to cart with id:{Car.id}"
        }
        return JsonResponse(data, status = 201)