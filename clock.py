from apscheduler.schedulers.blocking import BlockingScheduler
from chat import send_chat

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_chat, 'interval', seconds=10)

sched.start()