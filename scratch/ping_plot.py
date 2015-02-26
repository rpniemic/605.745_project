#!/usr/bin/env python

############################
# Brendan Byrne
# ping_plot.py
#
# This script must be run on a unix based system
# and have python 2.7 and matplotlib installed
#
# Example execution
# $ python ping_plot.py data1.txt data2.txt
#
# Feel free to mess around and see if you can 
# make this even better
############################

import matplotlib.pyplot as plt
import sys

def main ():
    if len(sys.argv) == 1: return
    
    raw_data = validate_inputs(sys.argv[1:])
    if raw_data is None: return
    
    # I chose to do a histogram plot of the data    
    plot_data(raw_data)
        
def plot_data (data):
    fig = plt.figure()
    
    plt.title('Histogram of measured rtt responses')
    plt.xlabel('rtt response (ms)')
    plt.ylabel('Number of occurances')
    
    for name, values in data.iteritems():
        plt.hist(values, bins = 200, label=name)
    
    plt.legend()
    plt.show()

def validate_inputs (inputs):
    try:
        data = dict()
        for filename in inputs:
            with open(filename, 'rb') as f:
                times = [float(line.strip()) for line in f]
            data[filename] = times
        return data
        
    except:
        return None

if __name__ == '__main__':
    main()
