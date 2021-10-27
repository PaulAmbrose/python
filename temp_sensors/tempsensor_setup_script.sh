#!/bin/bash

cd ~/
echo "dtoverlay=w1-gpio,gpiopin=4" >> /boot/config.txt
sudo modprobe w1-gpio
sudo modprobe w1-therm
cd /sys/bus/w1/devices

