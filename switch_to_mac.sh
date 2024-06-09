#!/bin/sh

source screens.sh

m1ddc display uuid=$LEFT set input 15 # DisplayPort 1
m1ddc display uuid=$MIDDLE set input 16 # USB-C / DisplayPort 2
m1ddc display uuid=$RIGHT set input 16 # USB-C / DisplayPort 2
