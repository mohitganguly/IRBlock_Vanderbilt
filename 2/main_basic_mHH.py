# Main basic file to run a simple NEURON-Python file. See manual for detailed instructions. 



from __future__ import division
from neuron import h
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#function to calculate derivatives of voltage and gating variables 
def deriv(a,b):
	der=[]
	if len(a)!=len(b):
		print ('cant calculate derivative')
	else:
		for i in range(len(a)-1):
			der.append((a[i+1]-a[i])/(b[i+1]-b[i]))
		return der
	der.append(der[-1])
	
def initialize():
	h.finitialize()
	
def integrate():
	while h.t<tstop:
		h.fadvance()


nseg = 7499
temp_x=np.genfromtxt('temp_x.csv',delimiter=',')

axon1=h.Section()
axon1.Ra = 35.4




axon1.nseg=nseg


dia=500
axon1.L=100000


x1 = np.linspace(0, axon1.L, axon1.nseg+1)


plt.plot(x1,temp_x)
plt.show()


axon1.insert('hh_pump')



#axon1.insert('hh')
#axon2.insert('hh')
#axon3.insert('hh')

#stim1=h.Ipulse2(0,sec=axon1) # repeated stimulations
stim1=h.IClamp(0,sec=axon1)  # for single stimultions
stim1.delay=50 #ms
stim1.dur=1#ms
stim1.amp=5000#nA


vec={}
for i in range(1,axon1.nseg+1):  # recording voltage traces at each node
	
	var_ina='ina1%d'%i
	var_ik='ik1%d'%i	
	var_i='i1%d'%i
	var_v = 'v1%d'%i
	var_gk = 'gk1%d'%i
		
	vec[var_ina]=h.Vector()
	vec[var_ik]=h.Vector()
	vec[var_gk]= h.Vector()
	vec[var_i]=h.Vector()
	
	#vec[var_gk].record(axon1(i/nseg)._ref_gk_hh_pump)
	vec[var_ina].record(axon1(i/nseg)._ref_ina)
	vec[var_ik].record(axon1(i/nseg)._ref_ik)
	vec[var_v]=h.Vector()
	vec[var_v].record(axon1(i/nseg)._ref_v)
	vec[var_i].record(axon1(i/nseg)._ref_i_hh_pump)
	
vec['t'] = h.Vector()
vec['t'].record(h._ref_t)		



h.dt=0.01
tstop=100

			
volt=[]	


#for i in range(1,nseg):     # assigniing temperature at each node
#	axon2(i/nseg).hh_pump.localtemp=temp_x[i]


t = []
t1=[]
t2=[]
for i in range(1, axon1.nseg+1):
	#print 1.60*np.exp(-np.power(((temp_x[i-1]-31.83)/31.62),2))
	
	t.append(-1*np.power(((temp_x[i-1]-29.02)/14.04),2))
 	t1.append(-1*np.power(((temp_x[i-1]-31.82)/31.62),2))
 	t2.append(-1*np.power(((temp_x[i-1]-15.75)/19.7),2))
	
	gkfit = 2*np.exp(t)
	gnafit = 0.35*np.exp(t1) + 0*np.exp(t2)
	
	axon1(i/nseg).gnabar_hh_pump = gnafit[i-1]
	axon1(i/nseg).gkbar_hh_pump = gkfit[i-1]
	axon1(i/nseg).localtemp_hh_pump = temp_x[i-1]

plt.plot(gkfit)
plt.plot(gnafit)
plt.show()

#plt.plot(gnafit)
#plt.show()

	

initialize()
integrate()

gk1 = []
gk2 = []
gk3 = []
vmax=[]
v=[]
for i in range(1, axon1.nseg+1):   #evaluating maximum voltages along the axon
	vmax.append(max(vec['v1%d'%i]))

	




plt.plot(x1/1000, temp_x, lw = 2)
plt.ylim((0, 45))
#plt.savefig('temp.png', format = 'png', dpi = 600)

plt.show()

plt.plot(vec['v12500'])
plt.plot(vec['v15000'])
plt.plot(vec['v17200'])
plt.show()


plt.plot(vec['ina11875'])
plt.plot(vec['ik11875'])
plt.show()
np.savetxt('ina_mHH_25.csv', vec['ina11875'], delimiter = ',')
np.savetxt('ik_mHH_25.csv', vec['ik11875'], delimiter = ',')
np.savetxt('i_mHH_25.csv', vec['i11875'], delimiter = ',')


plt.plot(vec['ina13750'])
plt.plot(vec['ik13750'])
plt.show()
np.savetxt('ina_mHH_50.csv', vec['ina13750'], delimiter = ',')
np.savetxt('ik_mHH_50.csv', vec['ik13750'], delimiter = ',')
np.savetxt('i_mHH_50.csv', vec['i13750'], delimiter = ',')

plt.plot(vec['ina15625'])
plt.plot(vec['ik15625'])
plt.show()
np.savetxt('ina_mHH_75.csv', vec['ina15625'], delimiter = ',')
np.savetxt('ik_mHH_75.csv', vec['ik15625'], delimiter = ',')
np.savetxt('i_mHH_75.csv', vec['i15625'], delimiter = ',')






#plt.subplot(5, 1, 2)
plt.plot(vmax)
plt.show()


#plt.plot(vec['t'], vec['v1499'], lw = 2)
#plt.plot(vec['t'], vec['v11250'], lw = 2)
#plt.plot(vec['t'], vec['v11999'], lw = 2)
#plt.xlim(45, 65)
#plt.savefig('volt.png', format = 'png', dpi = 600)
#plt.show()
#plt.subplot(5, 1, 4)
#plt.plot(vec['ina1499'])
#plt.plot(vec['ina11250'])

#plt.subplot(5, 1, 5)
#plt.plot(vec['ik1499'])
#plt.plot(vec['ik11250'])

##plt.savefig('HH_double_sigmoid.png', format = 'png', dpi = 600)
#plt.show()


