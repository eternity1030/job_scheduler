# job-scheduler

Details

  - Keeps track of jobs to be executed in future
  - Input for the script is an Array of Jobs like:
  ```
  [(job_1, delay_1), (job_2,delay_2) ..... ]
  ```
  - Output: Prints the jobId executed and the time it got executed.
  - Performance Metrics: Should be able to support 1000s of jobs.

### Things not Covered
  - Exception handling. If the input is not in the desired format then the script will break.
  - Logging: Printing the details like when the job got entered for scheduling to the console instead of logs.
  - Test cases.

# prerequisites
Install Python 2.7 type following command in the terminal window
  ```
  brew install python
  ```
  If you don't have homebrew, type following in the terminal window
  ```
  ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  ```

### Running the Script
After cloning the repository, go to the root and execute the following:
```
python scheduler.py
```

##### Input Format
At any time, you can add the jobs with following format
  ```
  [(job_1, delay_1), (job_2,delay_2) ..... ]
  EX:
  >> [(1,0), (2,3),(3,4)]
  ... jobs will get excuted ..
  [(4,6)]
  ```

![Alt text](input_format.jpg?raw=true "Title")


### Example

Following screenshot shows a part of execution flow.
Type "0" to exit.


![Alt text](execution_flow.jpg?raw=true "Title")
