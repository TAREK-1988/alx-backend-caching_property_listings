# alx-backend-caching_property_listings
Django property listings app demonstrating multi-level Redis caching (view-level + low-level), cache invalidation via signals, Redis metrics analysis, with Dockerized PostgreSQL and Redis.
# alx-backend-caching_property_listings

Django-based property listing application demonstrating multi-level Redis caching:
- View-level caching (15 minutes)
- Low-level caching for property queryset (1 hour)
- Cache invalidation using Django signals
- Redis cache metrics (hits/misses + hit ratio)
- Dockerized PostgreSQL and Redis services

## Tech Stack
- Django
- PostgreSQL
- Redis
- Docker Compose
- django-redis

## Endpoints
- `GET /properties/` -> returns list of properties (cached)

## Caching Strategy
1. View caching:
   - `@cache_page(60 * 15)` on the property list view
2. Low-level cache:
   - `cache.get('all_properties')` / `cache.set('all_properties', data, 3600)`
3. Invalidation:
   - `post_save` and `post_delete` signals delete `all_properties`

## Docker Services
- PostgreSQL: `postgres:latest` on port 5432
- Redis: `redis:latest` on port 6379

## Required Files (per ALX tasks)
- `alx_backend_caching_property_listings/settings.py`
- `docker-compose.yaml`
- `properties/models.py`
- `properties/views.py`
- `properties/urls.py`
- `properties/utils.py`
- `properties/signals.py`
- `properties/apps.py`
- `properties/__init__.py`
