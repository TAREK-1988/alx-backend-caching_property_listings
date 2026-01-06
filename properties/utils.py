import logging
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)


def get_redis_cache_metrics():
    try:
        redis_conn = get_redis_connection("default")
        info = redis_conn.info()

        hits = int(info.get("keyspace_hits", 0))
        misses = int(info.get("keyspace_misses", 0))
        total_requests = hits + misses

        hit_ratio = hits / total_requests if total_requests > 0 else 0

        logger.error(
            "Redis cache metrics - hits=%s misses=%s total=%s hit_ratio=%s",
            hits, misses, total_requests, hit_ratio
        )

        return {
            "hits": hits,
            "misses": misses,
            "hit_ratio": hit_ratio,
        }

    except Exception as exc:
        logger.error("Error getting Redis cache metrics: %s", exc)
        return {
            "hits": 0,
            "misses": 0,
            "hit_ratio": 0,
        }
