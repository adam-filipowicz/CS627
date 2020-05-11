from datetime import datetime
import argparse

next_year = datetime.now().year + 1
new_year = datetime(year=next_year, month=1,
                    day=1, hour=0, minute=0, second=0)
seconds_left = (new_year - datetime.now()).total_seconds()

welcome = "Calculate the number of days, hours, or minutes left in the year"
parser = argparse.ArgumentParser(description=welcome)
parser.add_argument('-u', '--unit', help="Enter 'days', 'hours', or 'minutes'")
args = parser.parse_args()

unit = args.unit

if unit == 'days':
    time_left = seconds_left / 86400
    print(f"There are {time_left} days left in the year")
if unit == 'hours':
    time_left = seconds_left / 3600
    print(f"There are {time_left} hours left in the year")
if unit == 'minutes':
    time_left = seconds_left / 60
    print(f"There are {time_left} minutes left in the year")
