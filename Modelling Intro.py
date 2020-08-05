"""Modelling Intro 8/3
    Owen LaFramboise"""

import random # Load in random module
import matplotlib.pyplot as plt # Load in matplotlib as plt


def moran_plot(starting_size_pop_A,starting_size_pop_B,fit_pop_A,generations,num_trials):
    """"Generates plot and matricies for a Moran Process with two populations"""
    fig, ax = plt.subplots() # Creates a figure with an axis
   
    
    for n in range(num_trials): # Will run the simulation as many times as the number of trials wanted
    
        size_pop_A=starting_size_pop_A # Resets the size of population A as the starting size
        size_pop_B=starting_size_pop_B # Resets the size of population B as the starting size
        col="" # Initializes the color of the plot
                
        popA=[size_pop_A] # Starts a list with the initial size of population A
        popB=[size_pop_B] # Starts a list with the initial size of population B
        x_axis=[0] # Starts a list with the number of generations at 0
                
        for x in range(generations): # Will run for the total number of generations
            
                if size_pop_A==0: # If there are no more individuals in population A, its size stays at 0
                    size_pop_B+=1 # Size of population B will now always increase by 1
                    popA+=[size_pop_A] # Add the new size of population A to the popA list
                    popB+=[size_pop_B] # Add the new size of population B to the popB list
                    x_axis+=[x] # Add the number of the generation to the generation list
                    #print([size_pop_A,size_pop_B]) # Print an array with each population size
                   
                
                elif size_pop_B==0: # If there are no more individuals in population B, its size stays at 0
                    size_pop_A+=1 # Size of population A will now always increase by 1
                    popA+=[size_pop_A] # Add the new size of population A to the popA list
                    popB+=[size_pop_B] # Add the new size of population B to the popB list
                    x_axis+=[x] # Add the number of the generation to the generation list
                    #print([size_popA,size_popB]) # Print an array with each population size
                    
                
                else: # If neither population is at 0
                    
                    if fit_pop_A*1000>=random.randint(1,1000): # Population A will gain a member
                        if fit_pop_A*1000>=random.randint(1,1000): # Population A will not lose a member
                            size_pop_A+=1 # Therefore the size of population A increases
                            size_pop_B-=1 # And the size of population B decreases
                        else: # Population A will lose a member
                            size_pop_A=size_pop_A # Therefore both populations stay the same size
                            size_pop_B=size_pop_B
                            
                        popA+=[size_pop_A] # Add the new size of population A to the pop1 list
                        popB+=[size_pop_B] # Add the new size of population B to the pop2 list
                        x_axis+=[x] # Add the number of the generation to the generation list
                        #print([size_pop_A,size_pop_B]) # Print an array with each population size
                        
                        
                    else: # Population B will gain a member
                        if fit_pop_A*1000>=random.randint(1,1000): # Population B will lose a member
                            size_pop_A=size_pop_A # Therefore both populations stay the same size
                            size_pop_B=size_pop_B
                        else: # Population B will not lose a member
                            size_pop_A-=1 # Therefore the size of population A decreases
                            size_pop_B+=1 # And the size of population B increases
                            
                        popA+=[size_pop_A] # Add the new size of population A to the pop1 list
                        popB+=[size_pop_B]# Add the new size of population B to the pop2 list
                        x_axis+=[x] # Add the number of the generation to the generation list
                        #print([size_pop_A,size_pop_B]) # Print an array with each population size
                        
                
                        
        if n==1: # Sets different colors of the plot for each trial 
            col="g"
        elif n==2:
            col='r'
        elif n==3:
            col='c'
        elif n==4:
            col='m'
        elif n==5:
            col='y'
        elif n==6:
            col='k'
        elif n==7:
            col='gray'
        elif n==8:
            col='purple'
        elif n==9:
            col="brown"
        else:
            col='b'    
                
               
                    
            
        ax.plot(x_axis,popA,label="Population A"+str(n),color=col) # Plot population A
        ax.plot(x_axis,popB,label="Population B"+str(n),color=col,linestyle='dashed') # Plot population B
        ax.legend(loc='upper left', bbox_to_anchor=(0.75, -0.05))
        ax.set_xlabel('Generations') # Set the x label
        ax.set_ylabel('Number of Individuals') # Set the y label
            




moran_plot(50,50,0.5,100,10)
        



        
        
        
