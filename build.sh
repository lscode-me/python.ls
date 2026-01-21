#!/bin/bash -e

build_html/build_html.sh
build_tma/build_tma.sh
rsync -avz html/ static_server:/mnt/en.lscode.me/dist/
