#!/bin/bash
# request to URL passed as argument using option -o and a path
curl -s -o /dev/random -w "%{http_code}" "$1"
