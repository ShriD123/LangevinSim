# This project is a generalized program used to conduct linear regression
# Shri Deshmukh July 2019

import math
import numpy as np

def linRegMSD(arrMSD, arrTime, log=False):
    ''' This function uses linear regression to calculate the MSD using a power law
    for a given set of data. Parameters will be an array of the MSD and an array of 
    time. The log variable indicates if the data has been already put into log space.
    Returns a tuple with the A value, then the n value.'''

    if (len(arrMSD) != len(arrTime)):
        raise ValueError('Input arrays must be of the same length.')
    
    arr1 = []        # MSD Array
    arr2 = []        # Time Array
    # Updating our arrays with respect to the data given
    for i in range(len(arrMSD)):
        if (not log):
            if (arrMSD[i] == 0.0):
                arr1.append(0.0)
            if (arrMSD[i] == 0.0):
                arr2.append(0.0)
            if (arrMSD[i] != 0.0 or arrTime[i] != 0.0):
                arr1.append(math.log(arrMSD[i]))
                arr2.append(math.log(arrTime[i]))
        else:
            arr1.append(arrMSD[i])
            arr2.append(arrTime[i])


    # Create a m x 2 matrix entirely of ones, then add the log time
    npArr = np.ones((len(arrTime), 2))
    for i in range(len(arrTime)):
        npArr[i, 1] = arr2[i]  

    # Matrix equation for the linear regression
    pseudoinverse = np.linalg.pinv(np.dot(npArr.T, npArr))
    intermediate = np.dot(pseudoinverse, npArr.T)
    cVector = np.dot(intermediate, arr1)
    
    valueA = math.exp(cVector[0])
    valueN = cVector[1]

    return (valueA, valueN)
    
def computeMean(arrNum):
    '''This function calculates the mean of an array of data and returns it.'''
    return sum(arrNum) / len(arrNum)

def computeVariance(arrNum):
    '''This function calculates the variance of an array of values and returns it.
    Note that standard deviation is just the square root of the variance. This function
    uses Bessel's correction to reduce bias (dividing by N-1).'''
    mean = computeMean(arrNum)
    num1 = 0.0
    for i in range(len(arrNum)):
        num1 += ((arrNum[i] - mean) ** 2)
    return num1 / (len(arrNum) - 1)




    



        


