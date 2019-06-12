import numpy as np

import matplotlib.pyplot as plt




width = 2
t=np.linspace(0,200,200/0.01+2)

t = t-1
i5mhh=np.genfromtxt('/home/mohit/IRBlock_Vanderbilt-master-2/paper_figs/J paper/combined/mHH/i5.csv', delimiter=',')
i15mhh=np.genfromtxt('/home/mohit/IRBlock_Vanderbilt-master-2/paper_figs/J paper/combined/mHH/i15.csv', delimiter=',')
i25mhh=np.genfromtxt('/home/mohit/IRBlock_Vanderbilt-master-2/paper_figs/J paper/combined/mHH/i25.csv', delimiter=',')
#i35mhh=np.genfromtxt('/home/mohit/IRBlock_Vanderbilt-master-2/paper_figs/J paper/combined/mHH/i35.csv', delimiter=',')

ina5mhh=np.genfromtxt('/home/mohit/IRBlock_Vanderbilt-master-2/paper_figs/J paper/combined/mHH/ina5.csv', delimiter=',')
ina15mhh=np.genfromtxt('/home/mohit/IRBlock_Vanderbilt-master-2/paper_figs/J paper/combined/mHH/ina15.csv', delimiter=',')
ina25mhh=np.genfromtxt('/home/mohit/IRBlock_Vanderbilt-master-2/paper_figs/J paper/combined/mHH/ina25.csv', delimiter=',')
#ina35mhh=np.genfromtxt('/home/mohit/IRBlock_Vanderbilt-master-2/paper_figs/J paper/combined/mHH/ina35.csv', delimiter=',')

ik5mhh=np.genfromtxt('/home/mohit/IRBlock_Vanderbilt-master-2/paper_figs/J paper/combined/mHH/ik5.csv', delimiter=',')
ik15mhh=np.genfromtxt('/home/mohit/IRBlock_Vanderbilt-master-2/paper_figs/J paper/combined/mHH/ik15.csv', delimiter=',')
ik25mhh=np.genfromtxt('/home/mohit/IRBlock_Vanderbilt-master-2/paper_figs/J paper/combined/mHH/ik25.csv', delimiter=',')
#ik35mhh=np.genfromtxt('/home/mohit/IRBlock_Vanderbilt-master-2/paper_figs/J paper/combined/mHH/ik35.csv', delimiter=',')


ina=[]
ik=[]

i5_na = i5mhh.copy()
i5_k=i5mhh.copy()
i5_na[i5_na>0]=0
i5_k[i5_na<0]=0
area_norm=np.trapz(i5_na,t,dx=0.001)
#area_norm = 1
ina.append(i5_na)
ik.append(i5_k)

i15_na = i15mhh.copy()
i15_k=i15mhh.copy()
i15_na[i15_na>0]=0
i15_k[i15_na<0]=0
ina.append(i15_na)
ik.append(i15_k)

i25_na = i25mhh.copy()
i25_k=i25mhh.copy()
i25_na[i25_na>0]=0
i25_k[i25_na<0]=0
ina.append(i25_na)
ik.append(i25_k)

print area_norm
#i35_na = i35mhh.copy()
#i35_k=i35mhh.copy()
#i35_na[i35_na>0]=0
#i35_k[i35_na<0]=0
#ina.append(i35_na)
#ik.append(i35_k)


plt.show()
T = [5,15,25]

T=np.array(T)
T2=T+width


areas_na=[]
areas_k=[]
k=0
for temp in T:
	area_na=np.trapz(ina[k],t,dx=0.001)/area_norm
	area_k=np.trapz(ik[k],t,dx=0.001)/np.abs(area_norm)
	areas_na.append(area_na)
	areas_k.append(area_k)
	k=k+1


#############################################################
ax = plt.subplot(3,4,1)
plt.plot(t,ina5mhh,label='$T_x = 5^o$C',lw=1)
#plt.text(56,0.8,'$T_x = 5^o$C')
#plt.legend()
#plt.xlabel('Time (ms)')
#plt.ylabel('Na Current (mA/cm$^2$)')
#plt.fill_between(t,hot5, where= hot5>0, facecolor='red', interpolate=True)
#plt.fill_between(t,hot5, where= hot5<0, facecolor='green', interpolate=True)
plt.xlim(50,60)
plt.ylim(-5,15)
ax.set_yticks([-5,15])
ax.set_xticklabels([])
ax.set_xticks([])
ax.set_xticklabels([])
ax.set_xticks([])
#plt.ylabel ('nA/cm$^2$', fontsize = 16)
#ax.set_yticklabels([])
#ax.set_yticks([])


ax = plt.subplot(3,4,2)
plt.plot(t,ik5mhh,label='$T_x = 5^o$C',lw=1)
#plt.legend()
plt.xlim(50,60)
plt.ylim(-5,15)

#plt.xlabel('Time (ms)')
#plt.ylabel('Na Current (mA/cm$^2$)')
#plt.fill_between(t,hot15, where= hot15>0, facecolor='red', interpolate=True)
#plt.fill_between(t,hot15, where= hot15<0, facecolor='green', interpolate=True)
#plt.text(56,0.8,'$T_x = 15^o$C')
ax.set_xticklabels([])
ax.set_xticks([])
ax.set_yticklabels([])
ax.set_yticks([])

ax = plt.subplot(3,4,3)
plt.plot(t,ina5mhh + ik5mhh,label='$T_x = 25^o$C',lw=1)
#plt.legend()
#plt.xlabel('Time (ms)')
#plt.ylabel('Na Current (mA/cm$^2$)')
#plt.text(56,0.8,'$T_x = 25^o$C')
plt.xlim(50,60)
#plt.fill_between(t,hot25, where= hot25>0, facecolor='red', interpolate=True)
#plt.fill_between(t,hot25, where= hot25<0, facecolor='green', interpolate=True)
plt.ylim(-5,15)
#plt.axhline(y=0, xmin=0, xmax=10, linewidth=1, color = 'k', linestyle = '--')
ax.set_xticklabels([])
ax.set_xticks([])
ax.set_yticklabels([])
ax.set_yticks([])

T = 5
ax = plt.subplot(3,4,4)
plt.bar(T-width,areas_na[0], width , color = 'green', label='Net inward current')
plt.bar(T,areas_k[0],  width, color='indianred', label='Net positive current')
ax.set_xticklabels([])
ax.set_xticks([])
plt.ylim(0,200)
ax.set_yticks([0,200])
print areas_k[0]/areas_na[0]
#plt.text(T - width/2, 8,str(float(areas_k[0]/areas_na[0]))[:4])
#############################################################################

ax = plt.subplot(3,4,5)
plt.plot(t,ina15mhh,label='$T_x = 5^o$C',lw=1)
#plt.text(56,0.8,'$T_x = 5^o$C')
#plt.legend()
#plt.xlabel('Time (ms)')
#plt.ylabel('K Current (mA/cm$^2$)')
#plt.fill_between(t,hot5, where= hot5>0, facecolor='red', interpolate=True)
#plt.fill_between(t,hot5, where= hot5<0, facecolor='green', interpolate=True)
plt.xlim(50,60)
plt.ylim(-5,15)
ax.set_xticklabels([])
ax.set_xticks([])
ax.set_yticks([-5,15])
#ax.set_yticklabels([])
#ax.set_yticks([])


ax = plt.subplot(3,4,6)
plt.plot(t,ik15mhh,label='$T_x = 15^o$C',lw=1)
#plt.legend()
plt.xlim(50,60)
plt.ylim(-5,15)
#plt.xlabel('Time (ms)')
#plt.ylabel('K Current (mA/cm$^2$)')
#plt.fill_between(t,hot15, where= hot15>0, facecolor='red', interpolate=True)
#plt.fill_between(t,hot15, where= hot15<0, facecolor='green', interpolate=True)
#plt.text(56,0.8,'$T_x = 15^o$C')

ax.set_xticklabels([])
ax.set_xticks([])
ax.set_yticklabels([])
ax.set_yticks([])

ax = plt.subplot(3,4,7)
plt.plot(t,ik15mhh + ina15mhh ,label='$T_x = 25^o$C',lw=1)
#plt.axhline(y=0, xmin=0, xmax=10, linewidth=1, color = 'k', linestyle = '--')
#plt.legend()
#plt.xlabel('Time (ms)')
#plt.ylabel('K Current (mA/cm$^2$)')
#plt.text(56,0.8,'$T_x = 25^o$C')
plt.xlim(50,60)
#plt.fill_between(t,hot25, where= hot25>0, facecolor='red', interpolate=True)
#plt.fill_between(t,hot25, where= hot25<0, facecolor='green', interpolate=True)
plt.ylim(-5,15)
ax.set_xticklabels([])
ax.set_xticks([])
ax.set_yticklabels([])
ax.set_yticks([])

T = 15
ax = plt.subplot(3,4,8)
plt.bar(T-width,areas_na[1], width , color = 'green', label='Net inward current')
plt.bar(T,areas_k[1],  width, color='indianred', label='Net positive current')
ax.set_xticklabels([])
ax.set_xticks([])
plt.ylim(0,200)
ax.set_yticks([0,200])
#plt.text(T - width/2, 8,str(float(areas_k[1]/areas_na[1]))[:4])
print areas_k[1]/areas_na[1]
#########################################################################################

ax = plt.subplot(3,4,9)
plt.plot(t,ina25mhh,label='$T_x = 5^o$C',lw=1)
#plt.text(56,0.8,'$T_x = 5^o$C')
#plt.legend()
#plt.xlabel('Time (ms)')
#plt.ylabel('Total Current (mA/cm$^2$)')
#plt.fill_between(t,hot5, where= hot5>0, facecolor='red', interpolate=True)
#plt.fill_between(t,hot5, where= hot5<0, facecolor='green', interpolate=True)
plt.xlim(50,60)
plt.ylim(-5,15)
ax.set_xticklabels([])
ax.set_xticks([])
ax.set_yticks([-5,15])
#ax.set_yticklabels([])
#ax.set_yticks([])


ax = plt.subplot(3,4,10)
plt.plot(t,ik25mhh,label='$T_x = 15^o$C',lw=1)
#plt.legend()
plt.xlim(50,60)
plt.ylim(-5,15)
#plt.xlabel('Time (ms)')
#plt.ylabel('Total Current (mA/cm$^2$)')
#plt.fill_between(t,hot15, where= hot15>0, facecolor='red', interpolate=True)
#plt.fill_between(t,hot15, where= hot15<0, facecolor='green', interpolate=True)
#plt.text(56,0.8,'$T_x = 15^o$C')
ax.set_xticklabels([])
ax.set_xticks([])
ax.set_yticklabels([])
ax.set_yticks([])

ax = plt.subplot(3,4,11)
plt.plot(t,i25mhh,label='$T_x = 25^o$C',lw=1)
#plt.axhline(y=0, xmin=0, xmax=10, linewidth=1, color = 'k', linestyle = '--')
#plt.legend()
#plt.xlabel('Time (ms)')
#plt.ylabel('Total Current (mA/cm$^2$)')
#plt.text(56,0.8,'$T_x = 25^o$C')
plt.xlim(50,60)
#plt.fill_between(t,hot25, where= hot25>0, facecolor='red', interpolate=True)
#plt.fill_between(t,hot25, where= hot25<0, facecolor='green', interpolate=True)
plt.ylim(-5,15)
ax.set_xticklabels([])
ax.set_xticks([])
ax.set_yticklabels([])
ax.set_yticks([])



T = 25
ax = plt.subplot(3,4,12)
plt.bar(T-width,areas_na[2], width , color = 'green', label='Net inward current')
plt.bar(T,areas_k[2],  width, color='indianred', label='Net positive current')
ax.set_xticklabels([])
ax.set_xticks([])

plt.ylim(0,200)
ax.set_yticks([0,200])
print areas_k[2]/areas_na[2]
#plt.text(T - width/2, 8,str(float(areas_k[2]/areas_na[2]))[:4])

plt.subplots_adjust(wspace = 0.36, hspace = 0.29)
plt.savefig('fig-3r.png',dpi=600, format = 'png', bbox_inches = 'tight')
plt.show()

#############################################################################################

#scale bar 
#ax = plt.subplot(3,4,1)
#plt.plot((0,1), (0,0))
#plt.plot((0,0),(0,1))
#plt.xlim(0, 10)
#plt.ylim(-4, 8)
#ax.set_xticklabels([])
#ax.set_xticks([])
#ax.set_yticklabels([])
#ax.set_yticks([])
#plt.show()




