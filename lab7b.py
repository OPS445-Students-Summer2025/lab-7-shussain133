#!/usr/bin/env python3
# Author ID: Shazma

from lab7a import Time, format_time, valid_time, sum_times

def change_time(time, seconds):
    time.second += seconds
    if not valid_time(time):
        while time.second >= 60:
            time.second -= 60
            time.minute += 1
        while time.second < 0:
            time.second += 60
            time.minute -= 1
        while time.minute >= 60:
            time.minute -= 60
            time.hour += 1
        while time.minute < 0:
            time.minute += 60
            time.hour -= 1
    return None
