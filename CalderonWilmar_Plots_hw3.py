#Se usó parte de la implementación de Matplotlib de los siguientes links:
#https://matplotlib.org/examples/animation/simple_anim.html  https://matplotlib.org/gallery/animation/random_walk.html 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.animation as animation

#importa los datos
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
#importa los datos.
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
ax = plt.axes(projection= '3d')
ax.plot_trisurf(xi1,yi1,zi1,cmap="jet",linewidths=0.2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Membrana del Tambor en $t=0$')
plt.tight_layout()
plt.savefig("condicioniniFF.pdf")

fig = plt.figure()
ax = plt.axes(projection= '3d')
ax.plot_trisurf(xi2,yi2,zi2,cmap="jet",linewidths=0.2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Membrana del Tambor en $t=0$')
plt.tight_layout()
plt.savefig("condicioniniFL.pdf")


fig = plt.figure()
ax = plt.axes(projection= '3d')
ax.plot_trisurf(xf1,yf1,zf1,cmap="jet",linewidths=0.2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Membrana del Tambor en $t=0.06$')
plt.tight_layout()
plt.savefig("condicionfinFF.pdf")

fig = plt.figure()
ax = plt.axes(projection= '3d')
ax.plot_trisurf(xf2,yf2,zf2,cmap="jet",linewidths=0.2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Membrana del Tambor con fronteras abiertas en $t=0.06$')
plt.tight_layout()
plt.savefig("condicionfinFL.pdf")


#Se realiza los cortes transversales para poderlos hacer en diferentes tiempos de la siguiente forma: clasifica primero los puntos en el intante t deseado y después se busca los x tal que se cumpla la condicion.
in10=np.where(t1==t1min)
in11=np.where(t1==0.009)
in12=np.where(t1==0.019)
in13=np.where(t1==0.029)
in14=np.where(t1==0.039)
in15=np.where(t1==0.049)
in16=np.where(t1==t1max)

in20=np.where(t2==t2min)
in21=np.where(t2==0.009)
in22=np.where(t2==0.019)
in23=np.where(t2==0.029)
in24=np.where(t2==0.039)
in25=np.where(t2==0.049)
in26=np.where(t2==t2max)



x10=x1[in10]
cxfa0=np.where(x10>-0.001)
xaux0=x1[cxfa0]
cxf0=np.where(xaux0<0.001)
y10=y1[in10]
z10=z1[in10]
ycf0=y10[cxf0]
zcf0=z10[cxf0]
x11=x1[in11]
cxfa1=np.where(x11>-0.001)
xaux1=x1[cxfa1]
cxf1=np.where(xaux1<0.001)
y11=y1[in11]
z11=z1[in11]
ycf1=y11[cxf1]
zcf1=z11[cxf1]
x12=x1[in12]
cxfa2=np.where(x12>-0.001)
xaux2=x1[cxfa2]
cxf2=np.where(xaux2<0.001)
y12=y1[in12]
z12=z1[in12]
ycf2=y12[cxf2]
zcf2=z12[cxf2]
x13=x1[in13]
cxfa3=np.where(x13>-0.001)
xaux3=x1[cxfa3]
cxf3=np.where(xaux3<0.001)
y13=y1[in13]
z13=z1[in13]
ycf3=y13[cxf3]
zcf3=z13[cxf3]
x14=x1[in14]
cxfa4=np.where(x14>-0.001)
xaux4=x1[cxfa4]
cxf4=np.where(xaux4<0.001)
y14=y1[in14]
z14=z1[in14]
ycf4=y14[cxf4]
zcf4=z14[cxf4]
x15=x1[in15]
cxfa5=np.where(x15>-0.001)
xaux5=x1[cxfa5]
cxf5=np.where(xaux5<0.001)
y15=y1[in15]
z15=z1[in15]
ycf5=y15[cxf5]
zcf5=z15[cxf5]
x16=x1[in16]
cxfa6=np.where(x16>-0.001)
xaux6=x1[cxfa6]
cxf6=np.where(xaux6<0.001)
y16=y1[in16]
z16=z1[in16]
ycf6=y16[cxf6]
zcf6=z16[cxf6]
plt.figure()
plt.subplot(241)
plt.plot(ycf0,zcf0)
plt.title("$t=0.0$")
plt.subplot(242)
plt.plot(ycf1,zcf1)
plt.title("$t=0.009$")
plt.subplot(243)
plt.plot(ycf2,zcf2)
plt.title("$t=0.019$")
plt.subplot(244)
plt.plot(ycf3,zcf3)
plt.title("$t=0.029$")
plt.subplot(245)
plt.plot(ycf4,zcf4)
plt.title("$t=0.039$")
plt.subplot(246)
plt.plot(ycf5,zcf5)
plt.title("$t=0.049$")
plt.subplot(247)
plt.plot(ycf6,zcf6)
plt.title("$t=0.059$")
plt.tight_layout()
plt.savefig("cortesfronterafija.pdf")

x20=x1[in20]
cxla0=np.where(x20>-0.001)
xaux01=x2[cxla0]
cxl0=np.where(xaux01<0.001)
y20=y2[in20]
z20=z2[in20]
ycl0=y20[cxl0]
zcl0=z20[cxl0]

x21=x2[in21]
cxla1=np.where(x21>-0.001)
xaux11=x2[cxla1]
cxl1=np.where(xaux11<0.001)
y21=y2[in21]
z21=z2[in21]
ycl1=y21[cxl1]
zcl1=z21[cxl1]

x22=x1[in12]
cxla2=np.where(x22>-0.001)
xaux21=x2[cxla2]
cxl2=np.where(xaux21<0.001)
y22=y2[in22]
z22=z2[in22]
ycl2=y22[cxf2]
zcl2=z22[cxf2]

x23=x2[in23]
cxla3=np.where(x23>-0.001)
xaux31=x2[cxla3]
cxl3=np.where(xaux31<0.001)
y23=y2[in23]
z23=z2[in23]
ycl3=y13[cxl3]
zcl3=z13[cxl3]

x24=x1[in24]
cxla4=np.where(x24>-0.001)
xaux41=x2[cxla4]
cxl4=np.where(xaux41<0.001)
y24=y2[in24]
z24=z2[in24]
ycl4=y24[cxl4]
zcl4=z24[cxl4]

x25=x2[in25]
cxla5=np.where(x25>-0.001)
xaux51=x1[cxla5]
cxl5=np.where(xaux51<0.001)
y25=y1[in25]
z25=z1[in25]
ycl5=y25[cxl5]
zcl5=z25[cxl5]

x26=x2[in26]
cxla6=np.where(x26>-0.001)
xaux61=x1[cxfa6]
cxl6=np.where(xaux61<0.001)
y26=y2[in26]
z26=z2[in26]
ycl6=y26[cxl6]
zcl6=z26[cxl6]
plt.figure()
plt.subplot(241)
plt.plot(ycl0,zcl0)
plt.title("$t=0.0$")
plt.subplot(242)
plt.plot(ycl1,zcl1)
plt.title("$t=0.009$")
plt.subplot(243)
plt.plot(ycl2,zcl2)
plt.title("$t=0.019$")
plt.subplot(244)
plt.plot(ycl3,zcl3)
plt.title("$t=0.029$")
plt.subplot(245)
plt.plot(ycl4,zcl4)
plt.title("$t=0.039$")
plt.subplot(246)
plt.plot(ycl5,zcl5)
plt.title("$t=0.049$")
plt.subplot(247)
plt.plot(ycl6,zcl6)
plt.title("$t=0.059$")
plt.tight_layout()
plt.savefig("cortesfronteralibre.pdf")

plt.figure()
plt.plot(ycf0,zcf0)
plt.title("Corte transversal en x=0.0 en $t=0.0$")
plt.savefig("corte.pdf")

