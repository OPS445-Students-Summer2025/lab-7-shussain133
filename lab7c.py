#!/usr/bin/env python3
# Author ID: Shazma


from lab7a import Time, valid_time

def format_time(t):
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def time_to_sec(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def sum_times(t1, t2):
    return sec_to_time(time_to_sec(t1) + time_to_sec(t2))

def change_time(time, seconds):
    total = time_to_sec(time) + seconds
    nt = sec_to_time(total)
    time.hour, time.minute, time.second = nt.hour, nt.minute, nt.second
    return None