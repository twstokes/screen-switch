#!/bin/sh

source screens.sh

m1ddc display uuid=$LEFT set input 17 # HDMI
m1ddc display uuid=$MIDDLE set input 15 # DisplayPort 1
m1ddc display uuid=$RIGHT set input 15 # DisplayPort 1

