import os
from apscheduler.schedulers.blocking import BlockingScheduler
from cicd_monitor_loop import check_github_actions
from log_monitor_loop import analyze_logs
from db_health_loop import check_table_growth

# Note: This manager uses APScheduler for demo. For production, use cron.
# Modify this script to start/stop jobs as needed.

scheduler = BlockingScheduler()

# Add jobs (intervals match the video)
scheduler.add_job(check_github_actions, 'interval', minutes=5, id='cicd')
scheduler.add_job(analyze_logs, 'interval', minutes=15, id='logs')
scheduler.add_job(check_table_growth, 'interval', hours=1, id='db')

# To list jobs
print('Active Jobs:')
for job in scheduler.get_jobs():
    print(f'ID: {job.id}, Next run: {job.next_run_time}')

# To stop a job, uncomment and modify:
# scheduler.remove_job('cicd')

print('Starting scheduler. Press Ctrl+C to stop.')
try:
    scheduler.start()
except KeyboardInterrupt:
    scheduler.shutdown()