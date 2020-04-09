#!/bin/bash
# A json is passed as argument in an send request with POST
curl -sX POST "$1" -d @"$2" -H "Content-Type: application/json"
