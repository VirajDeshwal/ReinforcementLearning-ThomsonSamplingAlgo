#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 17:31:58 2018

@author: virajdeshwal
"""



import matplotlib.pyplot as plt
import pandas as pd
import random

file = pd.read_csv('Ads_CTR_Optimisation.csv')
'''We are dealing with the different version of the same advertisement for the user'''
'''We have to find the CTR(Click through Rate )for the user. We have the clicks from 10000 users
and based on the clicks from 100k users we will choose which ads to show to the user.
'''

'''There is no library to implement Thomson Sampling  Algo.
We have to write it from scratch. Let's do it ;) '''

#implementing the Thomson Sampling ALgo
#Number of the users
N=10000
d=10
ads_selected = []
#defind the two variables 
numbers_of_rewards_1=[0]*d
numbers_of_rewards_0=[0]*d
sum_of_rewards = [0]*d
total_reward = 0

#we will loop all the selctions of the users 

for n in range(0,N):
    ad = 0
    max_upper_bound =0
    max_random=0
    #We need to compute of each version of the ads (the average reward and the confidence  interval)
    for i in range(0,d):
        random_beta =random.betavariate(numbers_of_rewards_1[i]+1, numbers_of_rewards_0[i]+1)
        if random_beta > max_random:
            max_random = random_beta
            ad =i
        ads_selected.append(ad)
       
        reward=file.values[n,ad]
        if reward==1:
            numbers_of_rewards_1[ad]= numbers_of_rewards_1[ad]+1
        else:
            numbers_of_rewards_0[ad] = numbers_of_rewards_0[ad] +1
        
        total_reward = total_reward +reward
        
        
#Now time for visualize the results
plt.hist(ads_selected)
plt.title('Histogram of Ads Selected')
plt.xlabel('Ads')
plt.ylabel('Number of time Ad was selected')
plt.show()

print('\n\n Done ;)')

        
    
