import time
current_time = time.time()

current_struct_time=time.gmtime(current_time)

print(current_struct_time)

current_hour = current_struct_time.tm_hour