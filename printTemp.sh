#!/bin/bash

hexCel=`sudo i2cget -y 1 0x48`
hexCel=${hexCel##*x}

decCel=`echo "obase=10; ibase=16; $hexCel" | bc`

fah=$(echo "scale=2;((9/5)*$decCel) + 32" |bc)
echo $fah
