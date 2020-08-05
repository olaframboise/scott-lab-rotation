"""Modelling Intro 8/3
    Owen LaFramboise"""

import random # Load in random module
import matplotlib.pyplot as plt # Load in matplotlib as plt


def moran_plot(size_pop1,size_pop2,fit_pop1,generations):
    """"Generates plot and matricies for a  Moran Process with two populations"""
    fig, ax = plt.subplots() # Creates a figure with an axis
    pop1=[size_pop1] # Starts a list with the initial size of population 1
    pop2=[size_pop2] # Starts a list with the initial size of population 2
    x_axis=[0] # Starts a list with the number of generations at 0
    
    for n in range(generations): # Will run for the total number of generations
        if fit_pop1*1000>=random.randint(1,1000): # Population 1 will gain a member
            if fit_pop1*1000>=random.randint(1,1000): # Population 1 will not lose a member
                size_pop1+=1 # Therefore the size of population 1 increases
                size_pop2-=1 # And the size of population 2 decreases
            else: # Population 1 will lose a member
                size_pop1=size_pop1 # Therefore both populations stay the same size
                size_pop2=size_pop2
                
            pop1+=[size_pop1] # Add the new size of population 1 to the pop1 list
            pop2+=[size_pop2] # Add the new size of population 2 to the pop2 list
            x_axis+=[n] # Add the number of the generation to the generation list
            print([size_pop1,size_pop2]) # Print an array with each population size
            
        else: # Population 2 will gain a member
            if fit_pop1*1000>=random.randint(1,1000): # Population 2 will lose a member
                size_pop1=size_pop1 # Therefore both populations stay the same size
                size_pop2=size_pop2
            else: # Population 2 will not lose a member
                size_pop1-=1 # Therefore the size of population 1 decreases
                size_pop2+=1 # And the size of population 2 increases
                
            pop1+=[size_pop1] # Add the new size of population 1 to the pop1 list
            pop2+=[size_pop2]# Add the new size of population 2 to the pop2 list
            x_axis+=[n] # Add the number of the generation to the generation list
            print([size_pop1,size_pop2]) # Print an array with each population size

    ax.plot(x_axis,pop1,label="Population 1") # Plot population 1
    ax.plot(x_axis,pop2,label="Population 2") # Plot population 2
    ax.legend() # Add a legend
    ax.set_xlabel('Generations') # Set the x label
    ax.set_ylabel('Number of Individuals') # Set the y label



moran_plot(50,50,0.5,100)



        
        
        
