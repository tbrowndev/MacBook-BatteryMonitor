import subprocess
import psutil
import time

# command to notify user of battery percentage
CMD = '''
on run argv
  display notification (item 2 of argv) with title (item 1 of argv)
  say (item 2 of argv)
end run
'''

# uses command with parameters to notify
# title: the title of the notification
# text: the description of the notification to speak
def notify(title, text):
  subprocess.call(['osascript', '-e', CMD, title, text])

while True:
  time.sleep(300)
  battery = psutil.sensors_battery()
  if battery.percent <= 20 and not battery.power_plugged: # Running on Battery. need to check if battery is low
    notify("Battery Monitor Alert", f'Low Battery Level: {battery.percent}%')
  elif battery.percent >= 90 and battery.power_plugged: # Running on AC Power. need to check if battery if fully charged. 
    notify("Battery Monitor Alert", f'Battery Level: {battery.percent}%')