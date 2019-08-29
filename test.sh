#!/bin/bash

if hash pytest 2>/dev/null; then
	echo # pytest avail
else
	source venv/bin/activate
fi

source export
cd tests
pytest
