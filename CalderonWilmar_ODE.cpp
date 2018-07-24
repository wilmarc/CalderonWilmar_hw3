#include <iostream>
#include<fstream>
#include <cmath>
#include <math.h>

using namespace std;

//Establece las constantes de todo el problema.
const float q=1.5;
const float m=2.5;
const float alpha=q/m;
const float b[3]={0.0,0.0,3.0};


//Nombra las funciones que serán utilizadas.
float ax(float vy,float vz);
float ay(float vx,float vz);
float az(float vx,float vy);

//Función Main del archivo
int main(){
//Declaración de tamaños de arreglos a usar con el intervalo de tiempo que se usará.
	int n=100000;
	float t0=0.0;
	float tf=15.0;
	float dt=((tf-t0)/n);
	float t[n];
	float x[n];
	float y[n];
	float z[n];
	float vx[n];
	float vy[n];
	float vz[n];

//Abre el archivo .txt sobre el cual se escribirán los datos.
	ofstream particula;
	particula.open("particula.txt");

//Creación de los distintos arreglos para las posiciones y velocidades en las componentes x, y y z.	

	for (int i=0;i<n;i++){
//Establecimiento de las condiciones iniciales.		
		if (i==0){
		t[i]=0.0;
		x[i]=1.0;
		y[i]=0.0;
		z[i]=0.0;
		float vxi=0.0;
		float vyi=1.0;
		float vzi=2.0;
//Como se usará el método de Leap-Frog, se inicializa el arreglo de velocidades en la posición "-1/2" para realizar pasos de 1 (Es decir el siguiente paso sería 1/2) con el fin de así calcular la posición futura.
		vx[i]=vxi+ax(vyi,vzi)*dt;
		vy[i]=vyi+ay(vxi,vzi)*dt;
		vz[i]=vzi+az(vxi,vyi)*dt;
		}
//Se usa el método de Leap-Frog para calcular las posiciones y velocidades (en sus componentes) futuras.
		else{
		x[i]=x[i-1]+vx[i-1]*dt;
		vx[i]=vx[i-1]+ax(vy[i-1],vz[i-1])*dt;

		y[i]=y[i-1]+vy[i-1]*dt;
		vy[i]=vy[i-1]+ay(vx[i-1],vz[i-1])*dt;
		
		z[i]=z[i-1]+vz[i-1]*dt;
		vz[i]=vz[i-1]+az(vx[i-1],vy[i-1])*dt;
		t[i]=t[i-1]+dt;
		}
//Escribe en el archivo particula.txt los datos de tiempo y posición para la partícula
	particula<<t[i]<<" "<<x[i]<<" "<<y[i]<<" "<<z[i]<<" " << endl;
	}

//Cierra el archivo.
particula.close();

return 0;
	
}

//Función definida como el producto cruz en la componente x (Equivalente a la Fuerza en la componente x) que multiplicado por alpha (q/m) Equivale a la aceleración en la componente x.
float ax(float vy,float vz){
	return alpha*(vy*b[2]-vz*b[1]);
}

//Función definida como el producto cruz en la componente y (Equivalente a la Fuerza en la componente y) que multiplicado por alpha (q/m) Equivale a la aceleración en la componente y.
float ay(float vx,float vz){
	return alpha*(vz*b[0]-vx*b[2]);
}

//Función definida como el producto cruz en la componente z (Equivalente a la Fuerza en la componente z) que multiplicado por alpha (q/m) Equivale a la aceleración en la componente z.
float az(float vx,float vy){
	return alpha*(vx*b[1]-vy*b[0]);
}






