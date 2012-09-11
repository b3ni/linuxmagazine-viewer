# -*- coding: utf-8 -*-
from config_celery import acquire_lock, release_lock


class TaskLockedMixin(object):
    """ Base para tareas periodicas """
    logger = None

    def run(self, *args, **kwargs):
        self.logger = self.get_logger(**kwargs)

        name_log = self.__class__.__name__.upper()
        name_lock = self.__class__.__name__.lower()

        self.logger.info(u"TASK: " + name_log)

        # LOCK
        lock_id = '%s-lock' % (name_lock)
        if not acquire_lock(lock_id):
            self.logger.info(u'%s (%s) running' % (name_log, lock_id))
            return

        # TASK
        try:
            self._do_task(*args, **kwargs)
        finally:
            release_lock(lock_id)

        self.logger.info(u"END: TASK " + name_log)

    def _do_task(self, *args, **kwargs):
        raise NotImplementedError()
