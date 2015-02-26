#!/usr/bin/env python

############################
# Brendan Byrne
# ping_parse.py
#
# This script must be run on a unix based system
# and have python 2.7 with argparse installed
#
# Example execution
# $ python ping_parse.py -a 192.168.1.130 -i 0.001 -c 1000 -o high_cpu
#
# Feel free to mess around and see if you can 
# make this even better
############################

import subprocess
import re
import argparse
from time import localtime, strftime

parser = argparse.ArgumentParser(description='Collects rtt data from ICMP message via ping then writes them to a file')
parser.add_argument('-a', '--ip', help = 'Address of device to ping')
parser.add_argument('-i', '--interval', type = float, help = 'The number of seconds between each ping.')
parser.add_argument('-c', '--count', type = int, help = 'The total number of pings to send')
parser.add_argument('-o', '--filename', help = 'The path of the output file')

def main ():
    command, filename = parse_inputs()
    try:
        raw = subprocess.check_output(command)        
        output = extract_times(raw)
        write_to_disk(output, filename)
    except:
        print 'Unexpected command termination'
        print 'You ran: {}'.format(' '.join(command))

def extract_times  (raw):
    
    key = r'time=(\d*.*\d*) ms'
    pattern = re.compile(key)
    
    output = [float(match) for match in pattern.findall(raw)]
    
    return output

def write_to_disk (output, filename):
    print 'Writing data to {}'.format(filename)
    with open(filename, 'a') as f:
        f.write('\n'.join( [str(num) for num in output] ))

def parse_inputs ():
    args = parser.parse_args()
    OUT_IP, max_attempts, rate = 'localhost', 10, 0.2
    
    if args.ip is not None: OUT_IP = args.ip
    
    if args.interval is not None: rate = args.interval
    
    if args.count is not None: max_attempts = args.count

    if args.filename is not None: filename = args.filename
    else: filename = '{}'.format(strftime('%Y-%m-%d_%H-%M-%S', localtime()))
    
    if rate < 0.2:
        command = ['sudo', 'ping', '-i', str(rate), '-c', str(max_attempts), OUT_IP]
    else:
        command = ['ping', '-i', str(rate), '-c', str(max_attempts), OUT_IP]
        
    return command, filename

if __name__ == '__main__':
    main()
