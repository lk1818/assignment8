'''
Created on Nov 7, 2015
Author: lk1818 
The main program prompts the user for two inputs: a list of positions and an integer of desired number of trials. 
The prompting process is done by the interaction module.
Then, the program creates an investSImulation class (defined in investment_simulation.py) with these inputs. 
With the generated class, the program generates desired histograms and plots.
'''

from matplotlib.pyplot import *
from numpy import *
from investment_simulation import *
from interaction import *

def main():
    # Prompts the user for a list of positions, and the number of trials.
    positions = get_positions()
    num_trials = get_num_trials()
    portfolio = investSimulation(positions, num_trials)
    
    # Write the result to result.txt
    text = open('results.txt', 'w')
    text.write(portfolio.pr)
    text.close()

    # Plot the returns of each position.
    for i in arange(len(positions)):
        zeroes = "0"*(4-len(str(positions[i])))
        hist(portfolio.daily_rets[i], 100, range = [-1, 1])
        savefig('histogram_' + zeroes + str(positions[i]) + '_pos.pdf')
        clf()


if __name__ == '__main__':
    main()
        
