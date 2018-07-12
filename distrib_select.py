#select by taking the top 20% of the probabilities
#how to get the top n items in a list and retain their index?
#do I need to?
#no, just take the top n items and those are the only ones we construct schedules with
#wrong, the item itself refers to the value of the PDF at that point, the index indicates the corresponding value
#so then we get
tot_trips = 121960
num_trips = [1911, 20185, 10947, 18979, 12646, 14006, 9568, 8603, 6139, 5035, 3742, 2786, 1986, 1521, 1093, 861, 543, 408, 312, 184, 124, 101, 83, 65, 32, 28, 20, 14, 9, 29]
tip_dist = [56.775, 25.454, 36.407, 40.191, 47.468, 53.282, 60.669, 65.124, 71.832, 78.508, 82.996, 89.712, 91.705, 99.293, 109.095, 107.939, 121.787,115.493,122.085,124.662,126.036,120.189,145.01,131.413,170.27,145.375,162.861,154.122,160.685,180.896]
deptime = [0.008434, 0.002108, 0, 0.002108, 0.002108, 0.003163, 0.032681, 0.239307, 0.286747, 0.102259, 0.043223, 0.061145, 0.042169, 0.045331, 0.045331, 0.036898, 0.028464, 0.022139,]
arrivtime = [0.01085702887, 0.009143038102, 0.007428568968, 0.004000109068, 0.004000109068, 0.004000109068, 0.002857289101, 0.008000218136, 0.02799980674, 0.02799980674, 0.02628581597, 0.03085709584, 0.04685705374, 0.05828573178, 0.06457148078, 0.05828573178, 0.07999978952, 0.08399989859, 0.09542857662, 0.09942868569, 0.1137141745, 0.08285707862, 0.03485720491, 0.01828559784]

def selection(distlist, topnum):
	#returns the top n% elements from distlist
	#distlist	- the list of distributions to be selected from
	#topnum		- top fraction of list to be returned
	maxlist = []
	for i in range(round(len(distlist)/(1/topnum))):
		m = max(distlist)
		index = [i for i,j in enumerate(distlist) if j == m]
		maxlist.append(index[0])
		distlist[index[0]] = 0
	return maxlist

