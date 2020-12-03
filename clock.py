from apscheduler.schedulers.blocking import BlockingScheduler
from chat import darisana

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(darisana, 'interval', seconds=10)

sched.start()