from numpy import *


''' This function computes the daily outcome of a single investment under simulation. '''
def get_individual_outc(position):
    position_value = 1000/position
    outc = empty([1, position], dtype = float)
    randm = random.random_integers(1, 100, position)
    outc[0, randm <= 51] = (position_value)*2
    outc[0, randm > 51] = 0
    return sum(outc)


''' This function computes the returns of repeated num_trials single-day investments under simulation. '''
def get_repeated_ret(position, num_trials):
    cumu_ret = empty([num_trials, 1], dtype = float)
    daily_ret = empty([num_trials, 1], dtype = float)
    for trial in arange(num_trials):
        cumu_ret[trial] = get_individual_outc(position)
        daily_ret[trial] = (cumu_ret[trial]/1000) - 1
    return daily_ret


''' Put together retuns of simulated trials of each positions. '''
def ret_by_positions(positions, num_trials):
    daily_rets = []
    for position in positions:
        daily_rets.append(get_repeated_ret(position, num_trials))
    return daily_rets

''' Compute expected values of each position. '''
def mean_by_positions(daily_rets):
    means = []
    for daily_ret in daily_rets:
        means.append(mean(daily_ret))
    return means


''' Compute standard deviation of each position. '''
def std_by_positions(daily_rets):
    stds = []
    for daily_ret in daily_rets:
        stds.append(std(daily_ret))
    return stds


''' Define a class to store the position array, number of trials, as well as daily returns, expected values, and standard deviations of each position. '''
class investSimulation():
    def __init__(self, positions, num_trials):
        self.positions = positions
        self.num_trials = num_trials
        self.daily_rets = ret_by_positions(self.positions, self.num_trials)
        self.means = mean_by_positions(self.daily_rets)
        self.stds = std_by_positions(self.daily_rets)
        self.pr = self.pr()
    
    def pr(self):  
        str_pr = ''
        for position in self.positions:
            i = self.positions.index(position)
            str_pr = str_pr + 'Position = %s:\nExpected Value of daily returns: %s\nStandard Deviation of daily returns: %s\n\n' % (position, self.means[i], self.stds[i])
        return str_pr 
    

    def __str__(self):
        return self.pr
    
