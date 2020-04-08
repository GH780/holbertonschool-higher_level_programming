#!/bin/bash
# A json is passed as argument in an send request with POST
curl "$1" -X POST -H "Content-Type: application/json" -d @"$2"
