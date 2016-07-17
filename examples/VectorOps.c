
public class ListaEnteros
{
private int [] v;
private int N;
public ListaEnteros() {
v = new int [1];
v[0]=0;
N=1;
}
public ListaEnteros(int n){
int j;
v = new int [n];
for (int i=0;i<=n-1;i++){
j = (int)(Math.random()*100+1);
v[i]=j;
}
N=n;
}
public ListaEnteros(int [] v) {
N=v.length;
this.v = new int [N];
for (int i=0; i<N; i++){
this.v[i] = v[i];
}
//this.v = v; opción a evitar.
}
public void escribe(){
for (int i=0; i<N; i++)
System.out.print(v[i]+" ");
System.out.println("*");
}
public ListaEnteros copia(){
ListaEnteros c = new ListaEnteros(N);
for (int i=0; i<=N-1; i++)
c.v[i]=v[i];
return c;
// return new ListaEnteros (this.v);
}
public int pares (){
int suma=0;
for (int i=0; i<N; i++)
if (v[i]%2==0) suma ++;
return suma;
}
public int primos (){
boolean primo;
int numPrimos=0;
for(int i=0; i<N; i++){
if ((v[i] == 1) || (v[i]==2)) {numPrimos ++; continue;}
primo = true;
for(int j=2; j<=v[i]/2; j++){
if (v[i]%j==0)
primo = false;
break;
}
if (primo) {numPrimos++;}
}
return numPrimos;
}
public ListaEnteros ordenaAsc(){
int temp;
for (int i=0; i<N-1; i++)
for (int j=N-1; j>i; j--)
if (v[j-1]>=v[j]){
temp=v[j-1];
v[j-1]=v[j];
v[j]=temp;
}
return this;
}
public void ordenaDesc(){
int temp;
for (int i=0; i<N-1; i++)
for (int j=N-1; j>i; j--)
if (v[j-1]<=v[j]){
temp=v[j-1];
v[j-1]=v[j];
v[j]=temp;
}
}
}