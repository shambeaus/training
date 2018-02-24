
uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

import pprint

DEBUG = True

# Easier to store these as constants
MINUTE_SECONDS = 60
HOUR_SECONDS = 60 * MINUTE_SECONDS
DAY_SECONDS = 24 * HOUR_SECONDS
WEEK_SECONDS = 7 * DAY_SECONDS
YEAR_SECONDS = 365 * DAY_SECONDS

uptime_dict = {}
uptime_dict2 = {}

for uptime in (uptime1, uptime2, uptime3, uptime4):

    uptime_fields = uptime.split(',')
    # Extract the hostname from uptime_fields
    (hostname, time_field1) = uptime_fields[0].split(' uptime is ')
    uptime_fields[0] = time_field1
    if DEBUG:
        print(hostname)
        print(uptime_fields)

uptimeseconds = 0

for i in uptime_fields:

    for string_match, time_factor in ((' year', YEAR_SECONDS), (' week', WEEK_SECONDS),
                                         (' day', DAY_SECONDS), (' hour', HOUR_SECONDS),
                                         (' minute', MINUTE_SECONDS)):
        if string_match in i:
            (time, na) = i.split(string_match)
            uptimeseconds += int(time) * time_factor
            print(uptimeseconds)

#    if 'year' in i:
#        (year, na) = i.split(' year')
#        try:
#            uptimeseconds += int(year) * YEAR_SECONDS
#        except ValueError:   
#            print('not a string')