#!/bin/sh
SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
EXTENSION="$SCRIPTPATH/.bashrc_extend"
cd
if grep -Fxq "source $EXTENSION" .bashrc;
then
    echo "Already appended once"
else
    echo "Adding to bashrc"
    echo "if [ -f $EXTENSION ]; then" >> .bashrc
    echo "source $EXTENSION" >> .bashrc
    echo "fi" >> .bashrc
fi
