#!/bin/bash

DefRoute=$(ip route show | grep -c '^default')

if [ "$DefRoute" -eq 1 ]; then
    echo "OK: Single default route detected"
elif [ "$DefRoute" -gt 1 ]; then
    echo "WARN: Multiple default routes detected"
else
    echo "ERROR: No default route found"
fi
