# -*- coding: utf-8 -*-
from django.core.cache import cache
import djcelery


BROKER_URL = "django://"    # tell kombu to use the Django database as the message queue
BROKER_BACKEND = "djkombu.transport.DatabaseTransport"

CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"

LOCK_EXPIRE = 60 * 10  # lock 10 minutos

# cache.add fails if if the key already exists
acquire_lock = lambda lock_id: cache.add(lock_id, 'true', LOCK_EXPIRE)
# memcache delete is very slow, but we have to use it to take
# advantage of using add() for atomic locking
release_lock = lambda lock_id: cache.delete(lock_id)

djcelery.setup_loader()
