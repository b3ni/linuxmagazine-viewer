#!/bin/bash

set -e

LOGFILE=/var/log/gunicorn/lvm-celery.log
LOGDIR=$(dirname $LOGFILE)

cd /usr/local/virtualenvs/lmv/lmv/
source ../bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR

exec ./manage.py celeryd -v 2 -B -s celery --events --loglevel=INFO --logfile=$LOGFILE 2>>$LOGFILE
