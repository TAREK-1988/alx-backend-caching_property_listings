import logging
from django.core.cache import cache
from django_redis import get_redis_connection

from .models import Property

logger = logging.getLogger(__name__)


def get_all_properties():
    cache_key = "all_properties"
    cached = cache.get(cache_key)
    if cached is not None:
        return cached

    qs = Property.objects.all().order_by("-created_at").values(
        "id", "title", "description", "price", "location", "created_at"
    )
    data = list(qs)

    cache.set(cache_key, data, 3600)  # 1 hour
    return data


def get_redis_cache_metrics():
    """
    Retrieve Redis INFO stats and calculate cache hit ratio.
    """
    try:
        conn = get_redis_connection("default")
        info = conn.info()

        hits = int(info.get("keyspace_hits", 0))
        misses = int(info.get("keyspace_misses", 0))
        total = hits + misses
        hit_ratio = (hits / total) if total > 0 else 0.0

        metrics = {
            "keyspace_hits": hits,
            "keyspace_misses": misses,
            "hit_ratio": round(hit_ratio, 4),
        }

        logger.info(
            "Redis cache metrics: hits=%s misses=%s hit_ratio=%s",
            hits, misses, metrics["hit_ratio"]
        )
        return metrics
    except Exception as exc:
        logger.exception("Failed to read Redis cache metrics: %s", exc)
        return {
            "keyspace_hits": 0,
            "keyspace_misses": 0,
            "hit_ratio": 0.0,
            "error": "metrics_unavailable",
        }
