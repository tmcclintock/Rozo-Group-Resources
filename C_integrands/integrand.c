#include<math.h>

double integrand(int n, double x){
  return cos(x)/(x*x*x);
}  

double integrand2(int n, double args[n]){
  double x = args[0];
  double a = args[1];
  double b = args[2];
  return cos(a*x)/pow(x,b);
}
