#!/bin/sh

NAME=${1%.*}
echo score name: $NAME

python3 transpiler.py $NAME.mc > $NAME.ly && \
    lilypond $NAME.ly && \
    atril $NAME.pdf
