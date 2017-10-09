# ****** REQUIREMENTS/NOTES ******
# queue keeping track of jobs to be executed in future ....
# Input : job id and time_delay
# output: printing job_id and current time ...
# Performance Metrics: should be able to support 1000s of jobs.

# ******* Approach Taken ***********
# > Maintaining a Hash where key is the timeStamp and value is an Array of jobs to be run at that particular time.
# > Created a timer that will look for Hash Key corresponding to current time O(1) and if Key found then will execute the jobs and then delete the key.
# ******* Things to Avoid *******
# > Looping through the given data structure, in order to maintain time & space complexity.
# > Not having too many Threads.



from datetime import datetime, timedelta
import time
import threading
tmr = None # keeping track of gobal timer obj.


class Scheduler(object):
    def __init__(self):
        self.scheduled_jobs = {} # Hash for storing Key=timeStamp and Value=[jobs]

    def schedule_job(self, job):
        self.add_task(job)

    def add_task(self, job):
        # ex: If the Job is (1,0) then the timeStamp Key will be nothing but current time.
        #       If Job is (2,5) then the timeStamo key = current_time + 5sec delay
        job_execution_key = (datetime.now() + timedelta(seconds=job[1])).strftime("%Y-%m-%d %H:%M:%S")

        # If there is already jobs scheduled to run for the above timeStamp Key then simply append the job to
        #   exiting list of pending Jobs.
        if job_execution_key in self.scheduled_jobs:
            job_lst = self.scheduled_jobs[job_execution_key]
            job_lst.append(job[0])
            self.scheduled_jobs[job_execution_key] = job_lst
        else:
            # Create a new entry and add job to be executed in time "x"
            self.scheduled_jobs[job_execution_key] = [job[0]]

        self.log_msg("Job:",  job[0], "added at: ", self.date_time())

    def run(self):
        global tmr
        tmr = threading.Timer(1,self.run)
        tmr.start()

        # At any given amount of time check for the timeStamp Key in the Hash.
        # If found then fetch the list of jobs and execute in the same order.
        # And once executed delete the Key.
        current_time = self.date_time()
        if current_time in self.scheduled_jobs:
            jobs_to_run = self.scheduled_jobs[current_time]
            self.log_msg("Ran Job(s): ", jobs_to_run, "at", current_time)

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
job_schedular.run()     # Start the timer ....

while(True):
    user_input = input(">> ")
    if user_input == 0:
        tmr.cancel()
        break
    else:
        for i in user_input:
            job_schedular.schedule_job(i)
