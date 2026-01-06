from django.http import JsonResponse
from django.views.decorators.cache import cache_page

from .utils import get_all_properties, get_redis_cache_metrics


@cache_page(60 * 15)
def property_list(request):
    properties = get_all_properties()

    # Optional: include metrics (useful for manual review/debugging)
    # You can remove this line if you want pure listing only.
    metrics = get_redis_cache_metrics()

    return JsonResponse(
        {
            "count": len(properties),
            "results": properties,
            "cache_metrics": metrics,
        },
        safe=False
    )
