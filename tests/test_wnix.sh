#!/bin/bash

pushd $(rootfs) >/dev/null

cat usr/share/cats.jpg | input

cat usr/share/bluecow.jpg | input

cat usr/share/redcow.jpg | input

cat usr/share/chicken.pdf | input | think | what etc/animals | head -1

cat usr/share/bluecow.jpg | input | think | what etc/animals | head -1

cat usr/share/bluecow.jpg | input | think | what etc/colors | head -1

answer=$(
    cat usr/share/soccer.jpg | input | think | what <(ls ./etc) | head -1
);  cat usr/share/soccer.jpg | input | think | what etc/$answer | head -1

cat usr/share/bluecow.jpg | input | think | what <(ls etc/) | head -1

cat usr/share/redcow.jpg | input | think | what <(ls usr/share) | head -1

find usr/share/ | grep 'cow' | think | what <(cat etc/colors) | head -n2

cat usr/share/cats.jpg | input "How many are there"

cat usr/share/cats.jpg | input "What animal is this?"

cat usr/share/cats.jpg | input "What animals are these?"

cat usr/share/cats.jpg | input "How many cats?"

cat usr/share/cats.jpg | input "How many dogs?"

url='https://en.wikipedia.org/wiki/Basketball'
echo "$url" | url | html | think | what etc/sports | head -1
curl -s "$url" | html | think | what etc/sports | head -1

popd >/dev/null
