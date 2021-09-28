from collections import deque


def cycles_check(jobs, interested_job_index, interested_job_cycles):
    job_cycles = []
    for i in range(len(jobs)):
        if jobs[i] < interested_job_cycles:
            job_cycles.append(jobs[i])
        elif jobs[i] == interested_job_cycles:
            if i <= interested_job_index:
                job_cycles.append(jobs[i])
    return job_cycles


def print_result(job_cycles):
    print(sum(job_cycles))


jobs = deque([int(s) for s in input().split(', ')])
interested_job_index = int(input())
interested_job_cycles = jobs[interested_job_index]
job_cycles = cycles_check(jobs, interested_job_index, interested_job_cycles)
print_result(job_cycles)
