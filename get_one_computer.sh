#!/usr/bin/env bash

egrep "^do_one " ~/mesa/assembla/{star,binary}/test_suite/do1_test_source | awk '{print $2}' | xargs -I{} mesa_test search "computer: $1 ; test_case: {}"
