import numpy as np

class subfleet:

    
    
    def generator( stats_array, properties_array, number_of_subfleets):
    #generates a dictionary with a cartesian product of all properties of subfleets
    #to do: make it recursive/general
        internaldict = {}
        for i in range(len(stats_array)):
            internaldict[stats_array[i]] = []
        for j in range(number_of_subfleets):
            for k in range(number_of_subfleets):
                for l in range(number_of_subfleets):
                    for m in range(number_of_subfleets):
                        internaldict[stats_array[0]].append(properties_array[0][j])            
                        internaldict[stats_array[1]].append(properties_array[1][k])
                        internaldict[stats_array[2]].append(properties_array[2][l])
                        internaldict[stats_array[3]].append(properties_array[1][m])
        return internaldict
	
    def test(names,vals,length):
        internaldict = {}
        for i in range(length):
            if len(vals)>0:
                subfleet.test(names[1:],vals[1:],length)
            else:
                internaldict[names[0]].append(vals[0][i])

    def dict2array(dictionary):
        array = []
        for key in dictionary:
            array.append(key)


names = ['deptime','returntime','number of trips','trip distance']
deptime = np.linspace(0,23,24)
returntime = np.linspace(0,23,24)
numtrip = np.linspace(0,23,24)
tipdist = np.linspace(0,23,24)
vals = [deptime.tolist(), returntime.tolist()]
d = subfleet.generator(names,vals,24)


