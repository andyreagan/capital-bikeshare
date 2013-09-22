#!/usr/bin/python
#
# build-network.py
#
# let's build the network

def loadData():
  # get a list of files in the data directory
  import subprocess
  dataRoot = '../data/'
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

def outputGephi(data):
  # output an edge list csv for gephi 'vertex1,vertex2,weight'
  pass

def main():
  # first load the data
  data = loadData()
  # print out csv's to be plotted in Gephi (next)
  outputGephi(data)


# only run submitted to interpreter
if __name__ == '__main__':
  main()



