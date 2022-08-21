#!/bin/bash
# use this to start/stop/restart/check status on the app

# Show usage information
usage() {
    echo "Usage:  bash $0 [-h] [start|stop|restart|status]
Options:
-h      Display this help message.
"
}

# Parse flags
SHOW_HELP=false
while getopts "h" FLAG; do
    case "${FLAG}" in
        h) SHOW_HELP=true ;;
        *) usage; exit 2 ;;
    esac
done
[ ${SHOW_HELP} = true ] && usage && exit 0

# exit on any failure
set -e

# set the working directory
cd $(dirname "$0")

CMD=$1
PID=`ps -fu $USER| grep "gunicorn: master" | grep -v "grep" | awk '{print $2; exit}'`

start() {
    # this will start the application in the background
    gunicorn --workers 2 --bind=0.0.0.0:5000 wsgi:app > logs/app.log 2>&1 &
}

stop() {
	kill -9 $PID
	echo "app has been stopped"
}

if [ "$CMD" == "status" ]; then
	if [ -z "$PID" ]; then
		echo "app is not running"
	else
		echo "app is running with pid $PID"
	fi
elif [ "$CMD" == "start" ] || [ "$CMD" == "restart" ]; then
	if [ ! -z "$PID" ]; then
		stop
    	echo "pausing to let gunicorn shut down before restarting..."
		sleep 3
	fi
	start
	echo "app is started"
elif [ "$CMD" == "stop" ]; then
	if [ -z "$PID" ]; then
		echo "app is not running"
	else
		stop
	fi
else
	echo "invalid command '${CMD}'. run app.sh -h for usage"
fi