import csv
from json import dumps
import redis
import time
 
def perf_bl(csv_file, n):

    r = redis.Redis()

    r.delete("bloom")
    r.bf().create("bloom", 0.01, 1700000)

    with open(csv_file, encoding = 'utf-8') as csvfile:
        my_reader = csv.DictReader(csvfile,delimiter='\t')
        my_data = [my_row for my_row in my_reader]
        #print(my_data)
        pres = dup = 0
        print('Start to create the bloom filter over',n,'inputs')
        # get the start time
        st = time.process_time()
        for my_row in my_data[0:n]:
            #print(my_row['M'])
            if not r.bf().exists("bloom", my_row['M']):
                r.bf().add("bloom", my_row['M'])
                pres = pres + 1
            else:
                dup = dup + 1
        # get the end time
        et = time.process_time()
        # get execution time
        res = et - st
        print('CPU Execution time:', res, 'seconds')
        print('We found',dup,'duplicates in the input')
        print()
        print('Wall time (also known as clock time or wall-clock time) is simply the total time')
        print('elapsed during the measurement. Itâ€™s the time you can measure with a stopwatch.')
        print('It is the difference between the time at which a program finished its execution and')
        print('the time at which the program started. It also includes waiting time for resources.')
        print()
        print('CPU Time, on the other hand, refers to the time the CPU was busy processing')
        print('the programâ€™s instructions. The time spent waiting for other task to complete')
        print('(like I/O operations) is not included in the CPU time. It does not include')
        print('the waiting time for resources.')
#Step 1
 
perf_bl("DEMO.csv", 140000)
