# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 11:44:56 2015

@author: Elan
"""

from pylab import *

"""define the membership function
My membership function only assesses one thing - distance from the number 4
Thus what I do is take the absolute distance from 4 to the paramater that is fed in
and I then divide it by 3 to get the percentage distance from 4 (3 being the furthest distance away any number can be)"""
def memfunc(avg):
    return ((avg - 4 + 0.0) / 3)
    
"""defining a quick way to get the avaerage of 2 numbers"""
def avg(a, b):
    return (abs(((a + b) + 0.0) / 2))
    
"""define a function that returns the number of possible rolls with a higher average than the given average"""
def numRolls(avg):
    return distrobution[(avg)]

"""Generate Distrobution"""
"""create a dictionary"""
distrobution = {}

"""loop through all possible distances"""
for i in arange(0, 1.1, (1.0/6)): 
    
    """start the counter at 0"""
    count = 0; 
    
    """loop through all possible dice rolls"""       """if the distance of the specific roll is smaller or eqaul 
                                                        than that of the instance being checked --> increment counter"""
    for j in range(1, 7):
        for k in range(j, 7):
            count += 1 if (avg(memfunc(j), memfunc(k)) <= (i * 1.01)) else 0 #the x 1.01 just accounts for floating point errors
            
    distrobution[(i)] = count
"""END Generage Distrobution"""

"""Generate 2 random numbers on interval [1, 6] to simulate two dice rolls"""
die1 = randint(1, 7)
die2 = randint(1, 7)

"""generate the fuzzy set by sending both dice rolls through the membership function and getting the average value"""
fuzzy_set = avg(memfunc(die1), memfunc(die2))

rolls_better_or_same = numRolls(fuzzy_set)

print 'die 1:', die1
print 'die 2:', die2
print 'membership value: ', fuzzy_set
print '\n'

print 'number of 2 dice re rolls that can do better or the same as current: ', rolls_better_or_same
print 'percentage chance to do better or the same: ', int(rolls_better_or_same * 100.0 / 21), '%'
print '\n'

count1 = 0
fuzzy_set1 = 0
avg_fuzzy_set1 = 0
bad_fuzzy_set1 = 0
for i in range(1, 7):
    temp_fuzzy = avg(memfunc(i), memfunc(die1))
    if (temp_fuzzy <= (fuzzy_set * 1.01)):
        count1 += 1

    avg_fuzzy_set1 += temp_fuzzy     
    
    if(temp_fuzzy > bad_fuzzy_set1):
        bad_fuzzy_set1 = temp_fuzzy
    
    if(temp_fuzzy < fuzzy_set1):
        fuzzy_set1 = temp_fuzzy
avg_fuzzy_set1 /= 6.0
perc_chance_of_improvement1 = int(count1 * 100.0 / 6)

print 'number of re rolls that can do better or the same as current if die 2 is rolled again: ', count1
print 'percentage chance to do better or the same: ', perc_chance_of_improvement1, '%'
print 'best membership value: ', fuzzy_set1
print 'worst membership value: ', bad_fuzzy_set1
print 'average membership value: ', avg_fuzzy_set1
print '\n'

count2 = 0
fuzzy_set2 = 0
avg_fuzzy_set2 = 0
bad_fuzzy_set2 = 0
for i in range(1, 7):
    temp_fuzzy = avg(memfunc(i), memfunc(die2))
    if (temp_fuzzy <= (fuzzy_set * 1.01)):
        count2 += 1

    avg_fuzzy_set2 += temp_fuzzy    
    
    if(temp_fuzzy > bad_fuzzy_set2):
        bad_fuzzy_set2 = temp_fuzzy
    
    if(temp_fuzzy < fuzzy_set2):
        fuzzy_set2 = temp_fuzzy
avg_fuzzy_set2 /= 6.0
perc_chance_of_improvement2 = int(count2 * 100.0 / 6)

print 'number of re rolls that can do better or the same as current if die 1 is rolled again: ', count2
print 'percentage chance to do better or the same: ', perc_chance_of_improvement2, '%'
print 'best membership value: ', fuzzy_set2
print 'worst membership value: ', bad_fuzzy_set2
print 'average membership value: ', avg_fuzzy_set2
print '\n'

if(bad_fuzzy_set2 < fuzzy_set or bad_fuzzy_set1 < fuzzy_set):
    if(bad_fuzzy_set1 < bad_fuzzy_set2):
        print 'roll die 2 again'
    else:
        print 'roll die 1 again'
elif(fuzzy_set * 100 >= 50 or perc_chance_of_improvement1 >= 50 or perc_chance_of_improvement2 >= 50):
    if(fuzzy_set * 100 >= perc_chance_of_improvement1 or fuzzy_set * 100 >= perc_chance_of_improvement2):
        print 'roll both again'
    elif(perc_chance_of_improvement1 > perc_chance_of_improvement2):
        print 'roll die 2 again'
    elif(perc_chance_of_improvement1 == perc_chance_of_improvement2):
        if(fuzzy_set1 + avg_fuzzy_set1 + bad_fuzzy_set1 > fuzzy_set2 + avg_fuzzy_set2 + bad_fuzzy_set2):
            print 'roll die 1 again'
        else:
            print 'roll die 2 again'
    else:
        print 'roll die 1 again'
else:
    print 'do nothing'

"""essentially my algorithim needs to see percentage chance of increase in average if both are rolled again and if 1 is rolled again"""
"""and if both of those are too low it must stay where it is, ie if both percentages are below 50?"""

"""If order doesnt matter there are 21 different dice rolls"""
"""The distrobution is as follows: 

distance from 4 : number of possiblities
0    : 3
0.5  : 5
1    : 5
1.5  : 3
2    : 3
2.5  : 1
3    : 1

"""