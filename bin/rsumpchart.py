#!/usr/bin/env python

# Raspi-sump, a sump pump monitoring system.
# Al Audet
# http://www.linuxnorth.org/raspi-sump/
#
# All configuration changes should be done in raspisump.conf
# MIT License -- http://www.linuxnorth.org/raspi-sump/license.html

import time
import raspisump.todaychart as chart


def main():
    '''Initiate todaychart.py module to graph sump pit activity.'''
    csv_file = "/home/pi/raspi-sump/csv/waterlevel-{}.csv".format(
        time.strftime('%Y%m%d')
        )
    filename = "/home/pi/raspi-sump/charts/today.png"
    bytes2str = chart.bytesdate2str('%H:%M:%S')
    chart.graph(csv_file, filename, bytes2str)

if __name__ == "__main__":
    main()
