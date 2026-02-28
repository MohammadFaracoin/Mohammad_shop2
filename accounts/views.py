from django.http import HttpResponse, JsonResponse
from .models import City

def edit_profile(request):
    return HttpResponse('<h1> edit profile</h1>')

def get_cities(request):
    province_id = request.GET.get('province_id')
    if not province_id:
        return JsonResponse({'error': 'province id is not valid'}, status=400)

    cities = City.objects.filter(province_id=province_id).values('id', 'title')
    return JsonResponse(list(cities), safe=False)


