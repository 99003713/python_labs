import pytest
from function3 import *


# # Check whether given string is isogram or not

def test_is_isogram_1():

    s = "Geek"
    val = is_isogram(s)
    assert False == val


def test_is_isogram_2():

    s = "Harod"
    val = is_isogram(s)
    assert True == val


#  Given a string, find the mexican wave

def test_maxican_wave_1():

    s = "abc"
    li = maxican_wave(s)
    assert ['Abc', 'aBc', 'abC'] == li


def test_maxican_wave_2():

    s = "xy"
    li = maxican_wave(s)
    assert ['Xy', 'xY'] == li


# Given a number, find the largest number by deleting single digit (order of digits will remain same)


def test_largest_by_deleting_1():

    n = 9230
    re = largest_by_deleting(n)
    assert 923 == re


def test_largest_by_deleting_2():

    n = 8905
    re = largest_by_deleting(n)
    assert 895 == re


# # Given a number, find the largest number by shuffling the digits


def test_largeby_suff_1():

    n = 8905
    re = largeby_suff(n)
    assert 9850 == re


def test_largeby_suff_2():

    n = 5004
    re = largeby_suff(n)
    assert 5400 == re


# Compute the word frequency in given message

def test_freqcount_1():

    s = "hi hello hi"
    li = freqcount(s)
    assert [('hi', 2), ('hello', 1)] == li


def test_freqcount_2():

    s = "hello om"
    li = freqcount(s)
    assert [('hello', 1), ('om', 1)] == li


# Correct the malformed time string , for e.g "5:70:65" to "6:11:05"

def test_malformed_time_1():

    time = "5:70:65"
    new_time = malformed_time(time)
    assert "6:11:5" == new_time


def test_malformed_time_2():

    time = "11:70:65"
    new_time = malformed_time(time)
    assert "12:11:5" == new_time


# # Correct the malformed date string , for e.g. "45/8/2018" to "14/9/2018"


def test_malformed_date_1():

    date = "45/8/2018"
    new_date = malformed_date(date)
    assert "14/9/2018" == new_date


def test_malformed_date_2():

    date = "32/9/2018"
    new_date = malformed_date(date)
    assert "2/10/2018" == new_date


# # Convert ip address from "a.b.c.d" format into integer
def test_new_add_1():

    add = "192.168.0.0"
    newadd = new_add(add)
    assert 3232235520 == newadd


def test_new_add_2():

    add = "192.168.0.1"
    newadd = new_add(add)
    assert 3232235521 == newadd


# # RGB to Hex conversion and vice versa, e.g. (255,0,255) into 0xFF00FF

def test_rgb_to_max_1():
    n = (255, 0, 255)
    ans = rgb_to_hex(n)
    assert "0xff0ff" == ans


def test_rgb_to_max_2():
    n = (255, 0, 0)
    ans = rgb_to_hex(n)
    assert "0xff00" == ans


# # Generate accumulated strings,e.g. abcd ==> A-Bb-Ccc-Dddd


def test_accum_1():

    s1 = "abcd"
    s2 = accum(s1)
    assert "A_Bb_Ccc_Dddd" == s2


def test_accum_2():

    s1 = "xy"
    s2 = accum(s1)
    assert "X_Yy" == s2
