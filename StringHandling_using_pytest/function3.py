from collections import Counter
import ipaddress

# Check whether given string is isogram or not


def is_isogram(str1):
    l = len(str1)
    str2 = str1.lower()
    str3 = sorted(str2)
    i = 0
    j = 0
    for i in range(l):
        for j in range(i+1, l):
            if(str3[i] == str3[j]):

                return False

    return True


# Given a string, find the mexican wave

def maxican_wave(s):
    li = []
    i = 0
    l = len(s)
    for i in range(l):
        u = s[i].upper()
        newstr = s[:i] + u + s[i+1:]
        li.append(newstr)
    return li


# Given a number, find the largest number by deleting single digit (order of digits will remain same)

def largest_by_deleting(n):

    li = []
    r = 0
    temp1 = n

    while(n > 0):
        r = n % 10

        li.append(r)
        n = n//10

    m = min(li)

    rev = 0
    r1 = 0
    while(temp1 > 0):
        r1 = temp1 % 10

        if(m == r1):

            temp1 = temp1//10
            continue
        else:

            rev = rev*10 + r1

            temp1 = temp1//10

    newrev = 0
    r2 = 0

    while(rev > 0):

        r2 = rev % 10

        newrev = newrev*10 + r2
        rev = rev//10

    return newrev


# Given a number, find the largest number by shuffling the digits

def largeby_suff(n):
    n1 = n
    li = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while(n1 != 0):
        r = n1 % 10
        li[r] = li[r]+1
        n1 = n1//10

    large = 0
    i = 0
    j = 0
    for i in range(9, -1, -1):
        for j in range(0, li[i]):
            large = large*10 + i
    return large


# Compute the word frequency in given message

def freqcount(s):

    freq = Counter(s.split()).most_common()
    return freq


# Correct the malformed time string , for e.g "5:70:65" to "6:11:05"

def malformed_time(s):
    a = s.split(":")
    hr = int(a[0])
    mi = int(a[1])
    se = int(a[2])
    if se >= 60:
        new_se = se % 60
        new_mi = mi + se//60
        mi = new_mi
    if mi >= 60:
        new_mi = mi % 60
        new_hr = hr + mi//60
    new_time = ""
    new_time = "{0}:{1}:{2}".format(new_hr, new_mi, new_se)

    return(new_time)


def malformed_date(d):
    a = d.split("/")
    d = int(a[0])
    m = int(a[1])
    y = int(a[2])
    mon = [1, 3, 5, 7, 8, 10, 11]
    Flag = True
    if d > 30 and m not in mon:
        nm = m + d//30
        nd = d % 30
        Flag = False
    elif d > 31 and m in mon:
        nm = m + d//31
        nd = d % 31
        Flag = False
    else:
        nm = m

    if Flag and m > 12:
        ny = y + m//12
        nm = m % 12
    elif not Flag and nm > 12:
        ny = y + nm//12
        nm = nm % 12
    else:
        ny = y

    new_date = ""
    new_date = "{0}/{1}/{2}".format(nd, nm, ny)
    return(new_date)


# Convert ip address from "a.b.c.d" format into integer


def new_add(a):
    try:
        a = int(a)
        b = ipaddress.ip_address(a)
    except:
        a1 = ipaddress.ip_address(a)
        return(int(a1))


# RGB to Hex conversion and vice versa, e.g. (255,0,255) into 0xFF00FF

def rgb_to_hex(n):

    a = "0x"
    for i in n:
        b = hex(i)
        b = b[2:]
        a = a + b
    return a

# Generate accumulated strings,e.g. abcd ==> A-Bb-Ccc-Dddd


def accum(s1):
    l = len(s1)
    i = 0
    j = 0
    s2 = ""
    for i in range(0, l):
        s2 = s2 + s1[i].capitalize()

        for j in range(0, i):
            s2 = s2 + s1[i]
        if(i != l-1):
            s2 = s2 + "_"

    return s2
