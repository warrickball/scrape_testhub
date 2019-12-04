#!/usr/bin/env bash

for NAME in "$@"
do
    echo "mesa_test search computer: ${NAME}; version: 12200-13000 > ${NAME}.json"
    mesa_test search "computer: ${NAME}; version: 12200-13000" > "${NAME}".json
done
