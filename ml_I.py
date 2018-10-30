# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 14:51:09 2018

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#4b
#load data and create setosa, virginica and versicolor datasets
dataset = r"C:\Users\User\Documents\Bauhaus\WS18\Machine Learning\Exercises\Fisher.txt"
data = pd.read_csv(dataset, sep='\t')
#    print(data['Type'])
setosa = data.loc[data['Type'] == 0]
#    print(setosa['PW'])
virginica = data.loc[data['Type'] == 1]
versicolor = data.loc[data['Type'] == 2]

#function to calculate and return mean
def mean():
    
#    compute mean value for setosa measurement
    setosa_pw_mean = setosa['PW'].mean()
    setosa_pl_mean = setosa['PL'].mean()
    setosa_sw_mean = setosa['SW'].mean()
    setosa_sl_mean = setosa['SL'].mean()
    
#    compute mean value for virginica measurement
    virginica_pw_mean = virginica['PW'].mean()
    virginica_pl_mean = virginica['PL'].mean()
    virginica_sw_mean = virginica['SW'].mean()
    virginica_sl_mean = virginica['SL'].mean()
    
#    compute mean value for versicolor measurement
    versicolor_pw_mean = versicolor['PW'].mean()
    versicolor_pl_mean = versicolor['PL'].mean()
    versicolor_sw_mean = versicolor['SW'].mean()
    versicolor_sl_mean = versicolor['SL'].mean()
    
    return [setosa_pw_mean, setosa_pl_mean, setosa_sw_mean, setosa_sl_mean]
    return [virginica_pw_mean, virginica_pl_mean, virginica_sw_mean, virginica_sl_mean]
    return [versicolor_pw_mean, versicolor_pl_mean, versicolor_sw_mean, versicolor_sl_mean]

    
#    print("The mean petal width is: ")
#    print(setosa_pw_mean, virginica_pw_mean, versicolor_pw_mean)
#    print("The mean petal length is: ")
#    print(setosa_pl_mean, virginica_pl_mean, versicolor_pl_mean)
#    print("The mean sepal width is: ")
#    print(setosa_sw_mean, virginica_sw_mean, versicolor_sw_mean)
#    print("The mean sepal length is: ")
#    print(setosa_sl_mean, virginica_sl_mean, versicolor_sl_mean)


#function to compute and return min and max values    
def max_min():
    
    setosa_pw_max = setosa['PW'].max()
    setosa_pl_max = setosa['PL'].max()
    setosa_sw_max = setosa['SW'].max()
    setosa_sl_max = setosa['SL'].max()
    
    virginica_pw_max = virginica['PW'].max()
    virginica_pl_max = virginica['PL'].max()
    virginica_sw_max = virginica['SW'].max()
    virginica_sl_max = virginica['SL'].max()
    
    versicolor_pw_max = versicolor['PW'].max()
    versicolor_pl_max = versicolor['PL'].max()
    versicolor_sw_max = versicolor['SW'].max()
    versicolor_sl_max = versicolor['SL'].max()
    
    setosa_pw_min = setosa['PW'].min()
    setosa_pl_min = setosa['PL'].min()
    setosa_sw_min = setosa['SW'].min()
    setosa_sl_min = setosa['SL'].min()
    
    virginica_pw_min = virginica['PW'].min()
    virginica_pl_min = virginica['PL'].min()
    virginica_sw_min = virginica['SW'].min()
    virginica_sl_min = virginica['SL'].min()
    
    versicolor_pw_min = versicolor['PW'].min()
    versicolor_pl_min = versicolor['PL'].min()
    versicolor_sw_min = versicolor['SW'].min()
    versicolor_sl_min = versicolor['SL'].min()
    
    return [setosa_pw_max, virginica_pw_max, versicolor_pw_max]
    return [setosa_pl_max, virginica_pl_max, versicolor_pl_max]
    return [setosa_sw_max, virginica_sw_max, versicolor_sw_max]
    return [setosa_sl_max, virginica_sl_max, versicolor_sl_max]

    return [setosa_pw_min, virginica_pw_min, versicolor_pw_min]
    return [setosa_pl_min, virginica_pl_min, versicolor_pl_min]
    return [setosa_sw_min, virginica_sw_min, versicolor_sw_min]
    return [setosa_sl_min, virginica_sl_min, versicolor_sl_min]



    print("The max petal width is: ")
    print(setosa_pw_max, virginica_pw_max, versicolor_pw_max)
    print("The max petal length is: ")
    print(setosa_pl_max, virginica_pl_max, versicolor_pl_max)
    print("The max sepal width is: ")
    print(setosa_sw_max, virginica_sw_max, versicolor_sw_max)
    print("The max sepal length is: ")
    print(setosa_sl_max, virginica_sl_max, versicolor_sl_max)
#    
    print("The min petal width is: ")
    print(setosa_pw_min, virginica_pw_min, versicolor_pw_min)
    print("The min petal length is: ")
    print(setosa_pl_min, virginica_pl_min, versicolor_pl_min)
    print("The min sepal width is: ")
    print(setosa_sw_min, virginica_sw_min, versicolor_sw_min)
    print("The min sepal length is: ")
    print(setosa_sl_min, virginica_sl_min, versicolor_sl_min)

#4c
    #plot of petal length  on the x-axis, and the sepal length  on the y-axis
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.scatter(setosa['PL'], setosa['SL'], c='red', label = 'setosa')
ax.scatter(virginica['PL'], virginica['SL'], c='green', label = 'virginica')
ax.scatter(versicolor['PL'], versicolor['SL'], c='blue', label = 'versicolor')

plt.title("Iris Dataset")
plt.xlabel("Petal Length")
plt.ylabel("Sepal Lenght")
plt.legend(loc = 'upper left')
plt.show()

#4d

#subset of the Iris data with sepal length and only the setosa and virginica classes
new_data = pd.concat([setosa, virginica],keys = ['setosa', 'virginica'])
new_data = new_data.drop(["PW","PL","SW"], axis = 1)
new_data['class']= np.where(new_data.Type > 0, 'virginica', 'setosa')

#Plot showing the attribute on the x-axis and the class on the y-axis.
plt.scatter(new_data['SL'], new_data['class'])
plt.show()


mean()
max_min()