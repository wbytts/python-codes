import time

'''
['_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone', 'asctime', 'ctime',
'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'monotonic_ns', 'perf_counter',
'perf_counter_ns', 'process_time', 'process_time_ns', 'sleep', 'strftime', 'strptime', 'struct_time', 'thread_time',
'thread_time_ns', 'time', 'time_ns', 'timezone', 'tzname']
'''
# print(dir(time))

print(time.asctime())
print(time.ctime())
print(time.daylight)
print(time.gmtime(120))

# time.sleep(秒数)
