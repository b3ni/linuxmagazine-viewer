#!/bin/bash

set -e

LOGFILE=/var/log/gunicorn/lmv.log
LOGDIR=$(dirname $LOGFILE)

cd /usr/local/virtualenvs/lmv/lmv/
source ../bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR

exec ../bin/gunicorn_django -c ../etc/gunicorn.conf --log-file=$LOGFILE 2>>$LOGFILE
