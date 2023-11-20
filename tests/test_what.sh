#!/bin/bash

# TODO: move this to test_what.py and put some of
# the things below as examples in the readme

pushd root >/dev/null

cat usr/share/cats.jpg | input

cat usr/share/bluecow.jpg | input

cat usr/share/redcow.jpg | input

cat usr/share/chicken.pdf | input | think | What etc/animals | head -1

cat usr/share/bluecow.jpg | input | think | What etc/animals | head -1

cat usr/share/bluecow.jpg | input | think | What etc/colors | head -1

answer=$(
    cat usr/share/soccer.jpg | input | think | What <(ls ./etc) | head -1
);  cat usr/share/soccer.jpg | input | think | What etc/$answer | head -1

cat usr/share/bluecow.jpg | input | think | What <(ls etc/) | head -1

cat usr/share/redcow.jpg | input | think | What <(ls usr/share) | head -1

find usr/share/ | grep 'cow' | think | What <(cat etc/colors) | head -n2

popd >/dev/null
