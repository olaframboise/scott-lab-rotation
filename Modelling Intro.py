"""Modelling Intro 8/3
    Owen LaFramboise"""

import random # Load in random module
import matplotlib.pyplot as plt # Load in matplotlib as plt


def moran_plot(starting_size_pop_A,starting_size_pop_B,fit_pop_A,fit_pop_B,generations,num_trials):
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
            
                if size_pop_A==0 or size_pop_B==0: # If there are no more individuals in population A or B, both sizes stay the same
                    popA+=[size_pop_A] # Add the size of population A to the popA list
                    popB+=[size_pop_B] # Add thesize of population B to the popB list
                    x_axis+=[x] # Add the number of the generation to the generation list
                    #print([size_pop_A,size_pop_B]) # Print an array with each population size
                    
                
                else: # If neither population is at 0
                    rand_int1=random.randint(1,1000) # set random integers as variables to be used to determine birth or death
                    rand_int2=random.randint(1,1000)
                    pop_freq_A=size_pop_A/(size_pop_A+size_pop_B) # Frequency of population A in entire population
                    pop_freq_B=size_pop_B/(size_pop_A+size_pop_B) # Frequency of population B in entire population
                    
                    prob_A_increases=((fit_pop_A*size_pop_A)/(fit_pop_A*size_pop_A+fit_pop_B*size_pop_B))*pop_freq_A # Probability that population A will gain a member and population B will lose a member
                    prob_B_increases=((fit_pop_B*size_pop_B)/(fit_pop_A*size_pop_A+fit_pop_B*size_pop_B))*pop_freq_B # Probability that population B will gain a member and population A will lose a member
                    #print("prob A increases:", str(prob_A_increases))
                    #print("prob B increases:", str(prob_B_increases))
                    
                    if prob_A_increases*1000>=rand_int1: # Population A gains a member and Population B loses a member
                        size_pop_A+=1 # Therefore the size of population A increases
                        size_pop_B-=1 # And the size of population B decreases
                            
                        popA+=[size_pop_A] # Add the new size of population A to the popA list
                        popB+=[size_pop_B] # Add the new size of population B to the popB list
                        x_axis+=[x] # Add the number of the generation to the generation list
                        #print([size_pop_A,size_pop_B]) # Print an array with each population size
                    
                        
                    elif prob_A_increases*1000+prob_B_increases*1000>=rand_int2 and rand_int2>prob_A_increases*1000: # Population A loses a member and Population B gains a member
                        size_pop_A-=1 # Therefore the size of population A decreases
                        size_pop_B+=1 # And the size of population B increases
                            
                        popA+=[size_pop_A] # Add the new size of population A to the popA list
                        popB+=[size_pop_B]# Add the new size of population B to the popB list
                        x_axis+=[x] # Add the number of the generation to the generation list
                        #print([size_pop_A,size_pop_B]) # Print an array with each population size
                        
                    else: # Both populations stay the same size
                        size_pop_A=size_pop_A
                        size_pop_B=size_pop_B
                        
                        popA+=[size_pop_A] # Add the new size of population A to the popA list
                        popB+=[size_pop_B]# Add the new size of population B to the popB list
                        x_axis+=[x] # Add the number of the generation to the generation list
                        
                        
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
                
            
        print('#######################')                   
        print('final popA for plot',str(n), popA)    
        print('final popB for plot',str(n), popB)    

        
        ax.plot(x_axis,popA,label="Population A"+str(n),color=col) # Plot population A
        ax.plot(x_axis,popB,label="Population B"+str(n),color=col,linestyle='dashed') # Plot population B
        ax.legend(loc='upper left', bbox_to_anchor=(0.75, -0.05))
        ax.set_xlabel('Generations') # Set the x label
        ax.set_ylabel('Number of Individuals') # Set the y label
            




moran_plot(10,1,0.5,0.5,100,20)
        



        
        
        
