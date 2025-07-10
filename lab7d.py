#!/usr/bin/env python3
# Author ID: Shazma

class Time:
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return Time(hours, minutes, seconds)

    def change_time(self, seconds):
        total = self.time_to_sec() + seconds
        nt = Time(total // 3600, (total % 3600) // 60, total % 60)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second

    def time_to_sec(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def valid_time(self):
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

def sec_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    sec = seconds % 60
    return Time(hours, minutes, sec)
