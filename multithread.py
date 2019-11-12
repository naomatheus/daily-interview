import _thread
import threading
import time

# _thread.start_new_thread(func, (),[])

#Define a function from the thread 

# This code executes an infinite loop, and will need to be keyboard interrupted (ctrl + c)

def print_time(thread_name,delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print( '%s: %s:' % (thread_name, time.ctime(time.time() ) ))

	if count >= 6:

		return 'done'
	return 'complete'

try: 
	_thread.start_new_thread( print_time, ("Thread-1",1))

	_thread.start_new_thread( print_time, ("Thread-2",2))

except Exception as err:
	print(err.args)
	raise

while True:
	pass

# Although it is very effective for low-level threading, the thread module is very limited compared to the newer threading module.

# Threading module

# threading.activeCount() − Returns the number of thread objects that are active.

# threading.currentThread() − Returns the number of thread objects in the caller's thread control.

# threading.enumerate() − Returns a list of all thread objects that are currently active.

# run() − The run() method is the entry point for a thread.

# start() − The start() method starts a thread by calling the run method.

# join([time]) − The join() waits for threads to terminate.

# isAlive() − The isAlive() method checks whether a thread is still executing.

# getName() − The getName() method returns the name of a thread.

# setName() − The setName() method sets the name of a thread.




