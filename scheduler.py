# ****** REQUIREMENTS/NOTES ******
# queue keeping track of jobs to be executed in future ....
# Input : job id and time_delay
# output: printing job_id and current time

from datetime import datetime, timedelta
import time
import threading
tmr = None

class Scheduler(object):
    def __init__(self):
        self.scheduled_jobs = {}

    def schedule_job(self, job):
        self.add_task(job)

    def add_task(self, job):
        job_execution_key = (datetime.now() + timedelta(seconds=job[1])).strftime("%Y-%m-%d %H:%M:%S")

        if job_execution_key in self.scheduled_jobs:
            job_lst = self.scheduled_jobs[job_execution_key]
            job_lst.append(job[0])
            self.scheduled_jobs[job_execution_key] = job_lst
        else:
            self.scheduled_jobs[job_execution_key] = [job[0]]

        self.log_msg("Job:",  job[0], "added at: ", self.date_time())

    def run(self):
        global tmr
        tmr = threading.Timer(1,self.run)
        tmr.start()

        current_time = self.date_time()
        if current_time in self.scheduled_jobs:
            jobs_to_run = self.scheduled_jobs[current_time]
            self.log_msg("Ran Job: ", jobs_to_run, "at", current_time, "\n")

            try:
                del self.scheduled_jobs[current_time]
            except KeyError:
                pass

    def date_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def log_msg(self, *msg):
        print msg

message = "Please enter the jobs in following format: \n \
[(x,y)] => where 'X' is the job and 'Y' is the delay. \n \
****************************************** \n \
To EXIT, please enter '0'  \n \
****************************************** \n "
print message

job_schedular = Scheduler()
job_schedular.run()

while(True):
    user_input = input(">> ")
    if user_input == 0:
        tmr.cancel()
        break
    else:
        for i in user_input:
            job_schedular.schedule_job(i)
