#include <iostream>
#include<fstream>
#include <cmath>
#include <math.h>

using namespace std;

int main(){

float data[10000];
ifstream ifs;
ifs.open("init.dat");
int i=0;
while(!ifs.eof()){
	ifs >> data[i];	
	i++;
}

int n=100;
float condinic[n][n];
for(int j=0;j<n;j++){
	for (int i=0;i<n;i++){
		condinic[j][i]=data[(j*n+i)];
	}
}
/**
for(int i=0;i<n;i++){
	for (int j=0;j<n;j++){
	cout<<condinic[0][j]<<endl;
	}
}**/
ofstream fronterafija;
fronterafija.open("frontfija.txt");

ofstream fronteralibre;
fronteralibre.open("frontlib.txt");
int l=1;
float dx=0.01;
float dy=0.01;
float c=300.0;
float t0=0.0;
float tf=0.06;
float dt=(0.01/300)/2.0;
float dtaux=0.001;
int nt=(tf)/dtaux;
float t[nt];
float upas[n][n];
float upre[n][n];
float ufut[n][n];
float x[n];
float y[n];
for (int i=0;i<n;i++){
	if (i==0){
	x[0]=-0.5;
	y[0]=-0.5;
	}
	else{
	x[i]=x[i-1]+dx;
	y[i]=y[i-1]+dy;
	}
//cout<<x[i]<<" "<<y[i]<<endl;
}
int cont1=0;
int cont2=0;
for (int k=0;k<=nt;k++){
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if (k==0){
				upas[i][j]=condinic[i][j];
				upre[i][j]=upas[i][j];
				t[k]=0.0;
			}
			else if(k==1){
				upre[i][j]=(0.5*(pow((c*dt/dx),2.0))*(upas[i+1][j]-2.0*upas[i][j]+upas[i-1][j]))+(0.5*(pow((c*dt/dy),2.0))*(upas[i][j+1]-2.0*upas[i][j]+upas[i][j-1]))+upas[i][j];      
				t[k]=t[k-1]+dtaux;
				upre[0][j]=condinic[0][j];
				upre[n-1][j]=condinic[n-1][j];
			
				upre[j][0]=condinic[j][0];
				upre[j][n-1]=condinic[j][n-1];
			}
			else{
				ufut[i][j]=((pow((c*dt/dx),2.0))*(upre[i+1][j]-2.0*upre[i][j]+upre[i-1][j]))+((pow((c*dt/dy),2))*(upre[i][j+1]-2.0*upre[i][j]+upre[i][j-1]))+2.0*upre[i][j]-upas[i][j];    
				cont1 ++;
				t[k]=t[k-1]+dtaux;
			}
		}
	}
	
	for(int s=0;s<n;s++){
		for (int p=0;p<n;p++){
			if (cont1>1){
			upas[s][p]=upre[s][p];
			upre[s][p]=ufut[s][p];
			}
		}
	}
	for(int p=0;p<n;p++){
		upre[0][p]=condinic[0][p];
		upre[n-1][p]=condinic[n-1][p];
		upre[p][0]=condinic[p][0];
		upre[p][n-1]=condinic[p][n-1];
	}
	for (int i=0;i<n;i++){
		for (int j=0;j<n;j++){
			
		fronterafija<<x[i]<<" "<<y[j]<<" "<<upre[i][j]<<" "<<t[k]<<endl;		
		}
	}
for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if (k==0){
				upas[i][j]=condinic[i][j];
				upre[i][j]=upas[i][j];
				t[k]=0.0;
			}
			else if(k==1){
				upre[i][j]=(0.5*(pow((c*dt/dx),2.0))*(upas[i+1][j]-2.0*upas[i][j]+upas[i-1][j]))+(0.5*(pow((c*dt/dy),2.0))*(upas[i][j+1]-2.0*upas[i][j]+upas[i][j-1]))+upas[i][j];      
				t[k]=t[k-1]+dtaux;
				upre[0][j]=condinic[0][j];
				upre[n-1][j]=condinic[n-1][j];
			
				upre[j][0]=condinic[j][0];
				upre[j][n-1]=condinic[j][n-1];
			}
			else{
				ufut[i][j]=((pow((c*dt/dx),2.0))*(upre[i+1][j]-2.0*upre[i][j]+upre[i-1][j]))+((pow((c*dt/dy),2))*(upre[i][j+1]-2.0*upre[i][j]+upre[i][j-1]))+2.0*upre[i][j]-upas[i][j];    
				cont2 ++;
				t[k]=t[k-1]+dtaux;
			}
		}
	}
	
	for(int s=0;s<n;s++){
		for (int p=0;p<n;p++){
			if (cont2>1){
			upas[s][p]=upre[s][p];
			upre[s][p]=ufut[s][p];
			}
		}
	}
	for(int p=0;p<n;p++){
		upre[0][p]=upre[1][p];
		upre[n-1][p]=upre[n-1-1][p];
		upre[p][0]=upre[p][0];
		upre[p][n-1]=upre[p][n-1-1];
	}
	for (int i=0;i<n;i++){
		for (int j=0;j<n;j++){
			
		fronteralibre<<x[i]<<" "<<y[j]<<" "<<upre[i][j]<<" "<<t[k]<<endl;		
		}
	}
}

fronterafija.close();
fronteralibre.close();
return 0;
}	
