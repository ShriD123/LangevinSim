# This project is a simulation of normalized Brownian motion
# Shri Deshmukh July 2019

import math
import numpy as np
import matplotlib.pyplot as plt
import statistics

class Particle:
    def __init__(self):
        '''Initialization function. Initializes particle with position at (0,0).'''
        self.position = [0, 0]                              # Holds current position of particle
        self.displacementArray = []                         # Holds position for every timestep of particle
        self.displacementArray.append(self.position)

    def getPosition(self, timeStep):
        '''Returns the position of the particle at a certain timestep as a list of 2 variables.'''
        return self.displacementArray[timeStep] 

    def updatePosition(self):
        '''This function updates the position based off the random step.'''
        noise = getRandomStep()
        pos1 = self.position[0] + (math.sqrt(timeStep) * noise[0])
        pos2 = self.position[1] + (math.sqrt(timeStep) * noise[1])
        self.position = [pos1, pos2]
        self.displacementArray.append(self.position)
    
    def computeSquaredDisplacement(self, currPosition):
        '''This function computes the squared displacement of a particle.'''
        assert len(currPosition) == 2
        disp = currPosition[0] * currPosition[0] + currPosition[1] * currPosition[1]
        return disp


def getRandomStep():
    ''' This function creates a random variable from a unit variance and
    zero mean Gaussian distribution and returns it. This represents the noise
    component of our simulation.'''
    randomX = np.random.normal(0.0, 1.0)
    randomY = np.random.normal(0.0, 1.0)
    return (randomX, randomY)


if __name__ == '__main__':
    numParticles = 1000                         # Number of total particles, keep as a power of 10
    particles = []                              # Stores the object references of all the particles
    timeStep = 0.01                             # Delta T in Euler Stepping Method
    totalTime = 1   
    showErrorBars = True


    # Filling the timePlot, which contains the list of the time value at every timestep in the sim
    timePlot = [0.0]
    for counter in range(int(totalTime / timeStep)):
        timePlot.append(timeStep * (counter + 1))


    # Running the actual simulation
    for i in range(numParticles):        
        newParticle = Particle()
        particles.append(newParticle)
        for j in range(int(totalTime / timeStep)):
            particles[i].updatePosition()  

        # This line indicates the progress of the simulation (using end='\r' to update same line)
        print(str(i + 1) + ' out of ' + str(numParticles) + ' particles calculated!', end='\r')  

    assert len(particles) == numParticles
    assert len(timePlot) == int(totalTime / timeStep) + 1


    # Calculating Mean Squared Displacement
    meanSqDisp = [0.0]
    for j in range(int(totalTime / timeStep)):
        meanSqDisp.append(0.0)
        for i in range(numParticles):
            position2 = particles[i].getPosition(j + 1)
            meanSqDisp[j + 1] += particles[i].computeSquaredDisplacement(position2)
        meanSqDisp[j + 1] /= numParticles
    
    assert len(meanSqDisp) == int(totalTime / timeStep) + 1
    

    # Plotting up to first 7 random walks 
    if (numParticles < 7):
        num1 = numParticles
    else:
        num1 = 7
    for u in range(num1):
        xPos = [0.0]
        yPos = [0.0]
        for v in range(int(totalTime / timeStep)):
            currPosition = particles[u].getPosition(v + 1)
            xPos.append(currPosition[0])
            yPos.append(currPosition[1])
        plt.plot(xPos, yPos)
    plt.title('Examples of Random Walks.')
    plt.show()


    # Plotting the simulation and the error bars
    if (showErrorBars):
        interval = int(len(meanSqDisp) // 10)
        error = [0]

        for a in range(int(totalTime / timeStep)):
            if ((a + 1) % interval != 0):
                error.append(0)              
                continue
            timeStepArr = []
            for b in range(numParticles):
                partPos = particles[b].getPosition((a + 1))            
                timeStepArr.append(particles[b].computeSquaredDisplacement(partPos))
            error.append(math.sqrt(statistics.computeVariance(timeStepArr)))

        assert(len(error) == int(totalTime / timeStep) + 1)

        plt.errorbar(timePlot, meanSqDisp, yerr=error, errorevery=interval, fmt='-k', 
        ecolor='g', capsize=5)
        plt.xlabel('Rescaled Time')
        plt.ylabel('Mean Squared Displacement')
        plt.title('Simulation & Error.')
        plt.show()


    # Plotting the simulation and the linear regression (Power law)
    (a, n) = statistics.linRegMSD(meanSqDisp, timePlot)
    xVarLinReg = np.linspace(0, totalTime + timeStep, len(timePlot) + 1)
    yVarLinReg = a * xVarLinReg ** n                    
    print('A = ' + str(a) + ', n = ' + str(n) + '\n')
    plt.plot(xVarLinReg, yVarLinReg, 'b--', label='Linear Regression.')

    plt.plot(timePlot, meanSqDisp, 'r', label='Simulation')
    plt.xlabel('Rescaled Time')
    plt.ylabel('Mean Squared Displacement')
    plt.show()



    



