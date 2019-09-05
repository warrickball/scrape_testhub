#!/usr/bin/env bash

tr -d '\n' < "$1" | sed 's/\]\[/\,/g'
