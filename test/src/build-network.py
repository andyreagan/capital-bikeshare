#!/usr/bin/python
#
# build-network.py
#
# let's build the network

def loadData(dataRoot):
  # get a list of files in the data directory
  import subprocess

  dataFileList = [dataRoot + tmp for tmp in subprocess.Popen(['ls',dataRoot],stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0].rstrip().split('\n')]
  # check the list has all the files
  print dataFileList

  # load the data into a list (this will work for the test)
  # for production, will need to use less memory
  data = []
  for dataFile in dataFileList:
    print 'loading ' + dataFile
    f = open(dataFile,'r')
    f.readline() # skip the first line
    for line in f:
      data.append(line.rstrip().split(','))
  
  print 'example entry'
  print data[1:2]
  print 'there are ' + str(len(data)) + ' entries in the data list'

  return data

def buildEdgeDataDict(data):
  # initialize dict for storing [[duration],[starttime],[endtime],[user],[type]]
  edgeData = dict()
  import re
  for ride in data:
    # strip the trip numbers
    start = re.search(ride[3],'([0-9]+)')
    destination = re.search(ride[4],'([0-9]+)')
    edgeKey = start + '-' + destination
    if edgeKey not in edgeData:
      edgeData[edgeKey] = [ride[0:3],ride[5:len(ride)]]
    else:
      edgeData[edgeKey] = edgeData[edgeKey]+[ride[0:3],ride[5:len(ride)]]

  return edgeData

def outputGephi(dataRoot,edgeData):
  # output an edge list csv for gephi 'vertex1,vertex2,weight'
  f = open(dataRoot+'/gephi.csv','w')
  f.write('FROM,TO,WEIGHT\n')
  for key in edgeData:
    # write the from num, to num, num trips
    f.write(key.split('-')[0]+','+key.split('-')[1]+','+len(edgeData[key][0])+'\n')
  f.close()

def main():
  dataRoot = '../data'
  # first load the data as a list of lists
  data = loadData(dataRoot)
  # make a dict of edges (key), and trip details (value) from the list
  # is this the best data structure for organizing by trips,
  # or should we not even build this a-proiri (search stored data for 
  # desired values every time) for enough data
  edgeData = buildEdgeDataDict(data)
  # print out csv's to be plotted in Gephi (next)
  outputGephi(dataRoot,edgeData)


# only run submitted to interpreter
if __name__ == '__main__':
  main()



