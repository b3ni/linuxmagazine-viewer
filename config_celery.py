# -*- coding: utf-8 -*-
from django.core.cache import cache
import djcelery

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"

LOCK_EXPIRE = 60 * 60 * 1  # lock 1 hours
# cache.add fails if if the key already exists
acquire_lock = lambda lock_id: cache.add(lock_id, 'true', LOCK_EXPIRE)
# memcache delete is very slow, but we have to use it to take
# advantage of using add() for atomic locking
release_lock = lambda lock_id: cache.delete(lock_id)

djcelery.setup_loader()
