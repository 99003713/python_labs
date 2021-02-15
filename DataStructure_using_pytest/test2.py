import pytest
from function2 import *



# # find a stray number from list.....................................................
def test_stray_1():
    li = [5, 5, 5, 1, 5, 5, 5]
    m = stray(li)
    assert 1 == m

def test_stray_2():    
    li =[5, 5, 5, 7, 5, 5, 5]
    m = stray(li)
    assert 7 == m

# close to its mean .............................................  
def test_find_1():
    li = [1, 2, 4, 5, 6, 7, 8]
    nearest = findmean(li)  
    assert 5 == nearest


def test_find_2():
    li = [7, 2, 4, 5, 6, 7, 8]
    nearest = findmean(li)   
    assert 6 == nearest


# Find the missing number, given the original list and modified one........................ 

def test_findmissing_1():

    li1 = [1,2,3,4,5,6]
    li2 = [1,2,4,5,6]
    li = findmissing(li1,li2)
    assert [3] == li

def test_findmissing_2():

    li1 = [1,2,3,4,5,6]
    li2 = [1,2,4,5]
    li = findmissing(li1,li2)
    assert [3,6] == li    

# fFind the ifference between two lowest numbers in the list..................................

def test_lowestnum_1():
    li = [1,2,3,4,5,6]
    diff = lowestnum(li)
    assert 1 == diff    
  

def test_lowestnum_2():
    li = [0,2,3,4,5,6]
    diff = lowestnum(li)
    assert 2 == diff    
  

# In a given list, count no.of elements smaller than their mean....................................  

def test_smallerthanmean_1():
    li = [0,2,4,6,10,12]
    total_smaller = smallerthanmean(li)
    assert 3 == total_smaller


def test_smallerthanmean_2():
    li = [-1,-2,0,2,4,6,10,12]
    total_smaller = smallerthanmean(li)
    assert 4 == total_smaller    


# Find the no.of people in a bus, given the data of people onboarding & alighting at each station................


def test_no_of_people_1():
    li1 = [1,4,2,2,5,7]
    li2 = [0,2,0,4,1,1]
    people = total_people(li1,li2)
    assert 13 == people

def test_no_of_people_2():
    li1 = [10,14,2,2,5,7]
    li2 = [0,2,0,4,1,1]
    people = total_people(li1,li2)
    assert 32 == people    

# Find the average speed of vehicle, given the distance travelled for fixed time intervals, e.g. [0, 0.1, 0.25, 0.45, 0.55, 0.7, 0.9, 1.0]    


def test_averagespeed_1():
    li = [0, 0.1, 0.25, 0.45, 0.55, 0.7, 0.9, 1.0]
    avg = averagespeed(li)
    assert  0.14285714285714285  == avg