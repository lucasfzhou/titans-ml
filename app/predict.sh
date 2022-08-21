#!/bin/bash
# example of prediction using API
# pass the path to an image, or the default of luce.jpg will be used
# of course, the app must be running for this to work

# Show usage information
usage() {
    echo "Usage:  bash $0 [-h] [-m model scale] [image path]
Options:
-h      Display this help message.
-m	    The model scale in [0, 7].
"
}

# Parse flags
SHOW_HELP=false
SCALE=4
while getopts "hm:" FLAG; do
    case "${FLAG}" in
        h) SHOW_HELP=true ;;
		m) SCALE=${OPTARG};;
        *) usage; exit 2 ;;
    esac
done
shift $((OPTIND-1))
[ ${SHOW_HELP} = true ] && usage && exit 0
((${SCALE} < 0 || $SCALE > 7)) && usage && exit 2

# exit on any failure
set -e

# set the working directory
cd $(dirname "$0")

if [ -z "$1" ]; then
	IMAGEPATH="../images/luce.jpg"
else
	IMAGEPATH=$1
fi

curl -F "image=@${IMAGEPATH}" "http://localhost:5000/api/predict?scale=${SCALE}&top_k=5"