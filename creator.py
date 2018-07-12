import numpy as np

'''
def generator( stats_array, properties_array, number_of_subfleets):
	
	return

class fleetcreate:
    def __init__(self,size):
        self.dep = []
        self.ret = []
        for i in range(size):
            for j in range(size):
                self.dep.append(i*24/size)
                self.ret.append(j*24/size)
'''
def rec(names, vals,r):
    if r > 0:
        for j in names:
            rec(names,vals,r-1)
            for i in range(len(names)):
                for k in range(len(names)):
                    internaldict[names[0]].append(vals[0][i])
                    internaldict[names[1]].append(vals[1][k])
    #internaldict[names[0]].append(vals[0])


def generator( stats_array, properties_array, number_of_subfleets):
    internaldict = {}
    for i in range(len(stats_array)):
        internaldict[stats_array[i]] = []
    for j in range(len(stats_array)):
        for k in range(number_of_subfleets):
            internaldict[stats_array[0]].append(properties_array[0][j])            
            internaldict[stats_array[1]].append(properties_array[1][k])
    return internaldict

names = ['a','b']
vals = [[1,2],[3,4]]
internaldict ={}
for i in range(len(vals)):
        internaldict[names[i]] = []

