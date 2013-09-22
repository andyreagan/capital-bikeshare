#!/usr/bin/python
#
# build-network.py
#
# let's build the network

# get a list of files in the data directory
import subprocess
dataRoot = '../data/'
dataFileList = [dataRoot + tmp for tmp in subprocess.Popen(['ls',dataRoot],stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0].rstrip().split('\n')]

print dataFileList
