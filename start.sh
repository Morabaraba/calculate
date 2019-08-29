#!/bin/bash
PORT=$1
HOST=$2
if [ -z "$1" ]
then
	PORT=8686
fi
if [ -z "$2" ]
then
	HOST=0.0.0.0
fi

if hash flask 2>/dev/null; then
	echo # flask avail
else
	source venv/bin/activate
fi

source export
flask run --port=$PORT --host=$HOST
