
# In a given list of elements, all elements are equal except the one.Write a code to find the odd man out (Stray number)
def stray(li):
    l = len(li)
    i = 0
    j = 0
    
    for i in range (l):
        for j in range (l):
            if(li[i] != li[j]):
                r = li[j]
                return r




# In a given list of elements, find the elements which is close to its mean

def findmean(li):
    li.sort()
    l = len(li)
    i = 0
    diff1 = 0
    diff2 = 0
    mean = sum(li)/l
    for i in li:
        if(li[i]>=mean):
            if((mean-li[i-1]) < (li[i]-mean)):
                return li[i-1]
            else:
                return li[i]    



# Find the missing number, given the original list and modified one........................ 

def findmissing(li1,li2):
    li = []
    li = list(set(li1)-set(li2))

    return li

     
#   Find the ifference between two lowest numbers in the list


def lowestnum(li):
    li.sort()
    diff = li[1]-li[0]
    
    return diff


# In a given list, count no.of elements smaller than their mean


def smallerthanmean(li):
    li.sort()
    l = len(li)
    i = 0
    count = 0
    mean = sum(li)/l
    for i in li:
        if(i<mean):
            count = count+1

    return count        



# Find the no.of people in a bus, given the data of people onboarding & alighting at each station


def total_people(li1,li2):

    i = 0
    sum1 = 0
    sum2 = 0
    sum = 0
    for i in li1:
        sum1 = sum1 + i
    for i in li2:
        sum2 = sum2 + i    
    sum = sum1-sum2
    
    print(sum)
    
    return sum


# Find the average speed of vehicle, given the distance travelled for fixed time intervals, e.g. [0, 0.1, 0.25, 0.45, 0.55, 0.7, 0.9, 1.0]    

def averagespeed(li):
    i = 0
    l = len(li)
    
    li2 = []
    for i in range(0,l-1):
        
        li2.append(li[i+1]-li[i])

    l2 = len(li2)
    sum = 0
    avg = 0
    for i in range(l2):
        sum = sum + li2[i]

    avg = sum/l2
     
    return avg 