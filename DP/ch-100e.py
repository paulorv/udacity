# Sleep Cycle Estimator

import sys

sleep_cycle = 90

wake_time = raw_input("Enter wake time (ie. 8:00 AM):")

wake_hour = wake_time[0:wake_time.find(":")]
wake_minute = wake_time[wake_time.find(":")+1:wake_time.find(":")+3]

if wake_minute != "00":
	wake_min = float(wake_minute) / 60
	wake_combo = (int(wake_hour) + wake_min) * 60
	suggested = wake_combo / sleep_cycle


print wake_hour, wake_combo
