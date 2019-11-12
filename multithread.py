import _thread
import threading
import time

# _thread.start_new_thread(func, (),[])

#Define a function from the thread 

def print_time(thread_name,delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print( '%s: %s:' % (thread_name, time.ctime(time.time() ) ))

	# return

try: 
	_thread.start_new_thread( print_time, ("Thread-1",1))

	_thread.start_new_thread( print_time, ("Thread-2",2))

except Exception as err:
	print(err.args)
	raise

while 1:
	pass