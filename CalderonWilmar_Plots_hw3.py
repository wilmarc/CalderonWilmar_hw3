#https://matplotlib.org/examples/animation/simple_anim.html  https://matplotlib.org/gallery/animation/random_walk.html 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

data=np.genfromtxt("particula.txt",delimiter=" ")
t=np.array(data[:,0])
x=np.array(data[:,1])
y=np.array(data[:,2])
z=np.array(data[:,3])

plt.figure()
plt.subplot(221)
plt.plot(x,y)
plt.title("$x$ contra $y$")
plt.xlabel("$x$")
plt.ylabel("$y$")

plt.subplot(222)
plt.plot(x,z)
plt.title("$x$ contra $z$")
plt.xlabel("$x$")
plt.ylabel("$z$")

plt.subplot(223)
plt.plot(t,y)
plt.title("$t$ contra $y$")
plt.ylabel("$y$")
plt.xlabel("$t$")
plt.tight_layout()
plt.savefig("subplotspartic.pdf")	

fig = plt.figure()
ax = fig.add_subplot(111,projection= '3d')
sc = ax.scatter(x,y,z,s=1,alpha=0.4)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.set_title('Posicion de la particula')
plt.tight_layout()
plt.savefig("posicion.pdf")


#SEGUNDA PARTE (SEGUNDO PUNTO)
dat1=np.genfromtxt("frontfija.txt",delimiter=" ")
x1=dat1[:,0]
y1=dat1[:,1]
z1=dat1[:,2]
t1=dat1[:,3]

dat2=np.genfromtxt("frontlib.txt",delimiter=" ")
x2=dat2[:,0]
y2=dat2[:,1]
z2=dat2[:,2]
t2=dat2[:,3]

t1min=np.min(t1)	
t1max=np.max(t1)
inmin1=np.where(t1==t1min)
inmax1=np.where(t1==t1max)
t2min=np.min(t2)	
t2max=np.max(t2)
inmin2=np.where(t2==t2min)
inmax2=np.where(t2==t2max)

xi1=x1[inmin1]
yi1=y1[inmin1]
zi1=z1[inmin1]
xi2=x2[inmin2]
yi2=y2[inmin2]
zi2=z2[inmin2]

xf1=x1[inmax1]
yf1=y1[inmax1]
zf1=z1[inmax1]
xf2=x2[inmax2]
yf2=y2[inmax2]
zf2=z2[inmax2]


fig = plt.figure()
ax = fig.add_subplot(111,projection= '3d')
sc = ax.plot(xi1,yi1,zi1,c='b')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Membrana del Tambor en $t=0$')
plt.tight_layout()
plt.savefig("condicioniniFF.pdf")

fig = plt.figure()
ax = fig.add_subplot(111,projection= '3d')
sc = ax.plot(xi2,yi2,zi2,c='b')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Membrana del Tambor en $t=0$')
plt.tight_layout()
plt.savefig("condicioniniFL.pdf")

fig = plt.figure()
ax = fig.add_subplot(111,projection= '3d')
sc = ax.plot(xf1,yf1,zf1,c='b')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Membrana del Tambor en $t=0.06$')
plt.tight_layout()
plt.savefig("condicionfinFF.pdf")

fig = plt.figure()
ax = fig.add_subplot(111,projection= '3d')
sc = ax.plot(xf2,yf2,zf2,c='b')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Membrana del Tambor con fronteras abiertas en $t=0.06$')
plt.tight_layout()
plt.savefig("condicionfinFL.pdf")

