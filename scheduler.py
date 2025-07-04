from apscheduler.schedulers.blocking import BlockingScheduler
from main import main

scheduler = BlockingScheduler()
scheduler.add_job(main, 'interval', minutes=10)

print("Scheduler started. Running every 10 minutes.")
scheduler.start()
