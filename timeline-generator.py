from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta, TH, SA
import calendar

def get_quarter_end_date(year, quarter):
    quarter_end_month = {1: 3, 2: 6, 3: 9, 4: 12}
    month = quarter_end_month[quarter]
    day = calendar.monthrange(year, month)[1]
    return datetime(year, month, day)

def get_next_weekday(date, weekdays):
    # weekdays is a list of integers where Monday is 0 and Sunday is 6
    days_ahead = (min((weekday - date.weekday()) % 7 for weekday in weekdays) + 7) % 7
    return date + timedelta(days=days_ahead)

def generate_milestones(year, quarter):
    milestones = {}
    
    cycle_start_date = get_quarter_end_date(year, quarter)
    milestones["Cycle Start Date"] = cycle_start_date
    
    submission_deadline = get_next_weekday(cycle_start_date + timedelta(days=7), [0, 1, 2])
    milestones["Submission Deadline"] = submission_deadline
    
    presentation_time = submission_deadline + relativedelta(weekday=TH(+1))
    milestones["Presentation Time"] = presentation_time.replace(hour=15, minute=0)
    
    distribution_deadline = presentation_time + timedelta(hours=24)
    milestones["Distribution Deadline"] = distribution_deadline
    
    snapshot_date = presentation_time + relativedelta(weekday=SA(+1))
    milestones["Snapshot Date"] = snapshot_date
    
    payout_date = snapshot_date + timedelta(days=5)
    milestones["Payout Date"] = payout_date
    
    return milestones

def format_milestones(milestones):
    formatted_milestones = {key: f"{value.strftime('%A, %Y-%m-%d %H:%M:%S')}" for key, value in milestones.items()}
    return formatted_milestones

# Prompt user for input
year = int(input("Enter the year: "))
quarter = int(input("Enter the quarter (1-4): "))

milestones = generate_milestones(year, quarter)
formatted_milestones = format_milestones(milestones)

for milestone, date in formatted_milestones.items():
    print(f"{milestone}: {date}")
