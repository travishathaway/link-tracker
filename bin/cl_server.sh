#! /bin/bash

LOGFILE=$1

if [ -z "$LOGFILE" ]; then
    echo "Please supply log file as the first argument"
    exit 1
fi

while true; do
    date=`date -Iseconds`
    url=`nc -l -p 8111 --allow localhost | grep "Referer:" | egrep -o 'http://.+'`
    echo "$date,$url" >> $LOGFILE
done
