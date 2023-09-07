"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1


def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	"""
	Recursive implementation of binary search.

	Params:
	  mylist....list to search
	  key.......search key
	  left......left index into list to search
	  right.....right index into list to search

	Returns:
	  index of key in mylist, or -1 if not present.
	"""
	### TODO
  #base case
	if left > right:
		return -1
    #make a new element bc binary search works by checking the middle values
	middle = (left + right) // 2

	if mylist[middle] == key:
		return middle
	elif mylist[middle] > key:
		return _binary_search(mylist, key, left, middle-1)
	else:
		return _binary_search(mylist, key, middle+1, right)
	#if mylist[middle] == key:
	#	return middle #if the middle num (starting pt) is the key we dont need to keep searching
	#elif mylist[middle] < key: #if middle is smaller than key, move right (higher)
	#	return _binary_search(mylist, middle + 1, right, key)
  #elif mylist[middle] > key:
  #  return _binary_search(mylist, left, middle - 1, key)
  #else:
	#	return -1 #element not in list
	###

def time_search(search_fn, mylist, key):
	"""
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `sort_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""
	### TODO
	start = time.time() * 1000
	#start_readable = time.ctime(start)
	#time.sleep(1) #may or may not be necessary
	search_fn(mylist, key)
	end = time.time() * 1000
	#end_readable = time.ctime(start)
	diff = end - start
	return diff
  
	###

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	"""
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order. 

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""
	### TODO
	results = []
	for size in sizes:
		test_list = list(range(int(size)))
		results.append((size, time_search(linear_search, test_list, -1), time_search(binary_search, test_list, -1)))
	return results

		#create_list = ()
		#search_list = create_list(0, int(float(size)) - 1)
		#linear_search_time = time_search(linear_search, search_list, -1)
		#binary_search_time = time_search(binary_search, search_list, -1)
		#results.append(linear_search_time)
		#results.append(binary_search_time)

	#time_search(compare_search,sizes,-1)
  
	###

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))
print_results(compare_search())
