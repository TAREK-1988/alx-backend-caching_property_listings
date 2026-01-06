from django.http import JsonResponse
from django.views.decorators.cache import cache_page

from .models import Property


@cache_page(60 * 15)
def property_list(request):
    properties_qs = Property.objects.all().values(
        "id",
        "title",
        "description",
        "price",
        "location",
        "created_at",
    )
    data = list(properties_qs)
    return JsonResponse({"data": data})
