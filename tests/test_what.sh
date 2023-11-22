#!/bin/bash

# TODO: move this to test_what.py and put some of
# the things below as examples in the readme

pushd root >/dev/null

cat usr/share/cats.jpg | input

cat usr/share/bluecow.jpg | input

cat usr/share/redcow.jpg | input

cat usr/share/chicken.pdf | input | think | what etc/animals | head -1

cat usr/share/bluecow.jpg | input | think | what etc/animals | head -1

cat usr/share/bluecow.jpg | input | think | what etc/colors | head -1

printf "red cow\nblue cow\npurple chicken\ngreen chicken\n" | think -l | what etc/animals

printf "red cow\nblue cow\npurple chicken\ngreen chicken\n" | think -l | what etc/colors

answer=$(
    cat usr/share/soccer.jpg | input | think | what <(ls ./etc) | head -1
);  cat usr/share/soccer.jpg | input | think | what etc/$answer | head -1

cat usr/share/bluecow.jpg | input | think | what <(ls etc/) | head -1

cat usr/share/redcow.jpg | input | think | what <(ls usr/share) | head -1

find usr/share/ | grep 'cow' | think | what <(cat etc/colors) | head -n2

{ cat << EOF
red cow
blue cow
purple chicken
green chicken
EOF
 } | think -l | what etc/animals

popd >/dev/null
