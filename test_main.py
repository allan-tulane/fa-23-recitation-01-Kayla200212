from main import *


def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

###given this list, it looks for 5 at index 4
###
def test_binary_search():
	assert binary_search([1,2,3,4,5], 5) == 4 
	assert binary_search([1,2,3,4,5], 1) == 0
	assert binary_search([1,2,3,4,5], 6) == -1
	### TODO: add two more tests here.
	assert binary_search([1,3,5,7,9], 3) == 1
	assert binary_search([3,5,8,10,13,16,18,19], 19) == 7
	###


def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1
