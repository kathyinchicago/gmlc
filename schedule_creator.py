times = [[5,17],[6,19]]
timedesc = ["Home","Work","Home"]
schedule = []

def eventappend(vector,part,prevpart,descriptor,tempvec):
	for i in range(vector[part]-vector[prevpart]):
		tempvec.append(descriptor)

def events(avec,descriptions):
	for i in range(len(avec)):
		timevec = []
		for j in range(avec[i][0]):
			timevec.append("Home")
		eventappend(avec[i],1,0,descriptions[1],timevec)
		for l in range(24-avec[i][1]):
			timevec.append("Home")
		schedule.append(timevec)

