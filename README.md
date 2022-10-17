# MacBook Battery Monitor

This project checks the battery percentage and alerts the user through a notification of the battery level if over 90% or less than 20%

Why I created this:
- grew tired of leaving my computer on the charger too long when its already fully charged.
- wanted a way to know my battery level without having to check each time its it fully charged or about to die.

Dependencies
- subprocess: (used to display the notification to the user)
- psutil: ( used to check the battery levels and if plugged in or not)
- time