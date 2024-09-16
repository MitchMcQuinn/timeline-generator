# timeline-generator

This script follows these steps:

1) Get the Quarter End Date: Determines the last day of the specified quarter.
2) Calculate Submission Deadline: Finds the first Tuesday at least 7 days after the cycle start date.
3) Set Presentation Time: Schedules it for the Thursday following the submission deadline at 3:00 PM.
4) Determine Distribution Deadline: Sets it 24 hours after the presentation time.
5) Schedule Snapshot Date: Sets it on the Saturday following the presentation time.
6) Set Payout Date: Schedules it 5 days after the snapshot date.
git
You can run this script by specifying the year and quarter variables. The output will be formatted milestones with their respective dates and times.
