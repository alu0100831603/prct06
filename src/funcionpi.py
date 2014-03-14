#!/usr/bin/python
import sys
PI = 3.1415926535897931159979634685441852
def funcion(n):
   suma=0.0
   for i in range(1,n+1):
     x_i=float(i-1.0/2)/n
     #print'El valor de x_i es: %f' % x_i
     #print'Subintervalos: ', [(i-1)/float(n),i/float(n) ]
     fx_i= 4.0/(1+x_i**2)
     suma=suma+fx_i
     #print'El valor de f(x_i) es: %f' % fx_i
   pi = (1.0/float(n))*suma
   #print'El v1alor de pi es:pi=%.35f' %  pi

   #PI = 3.1415926535897931159979634685441852
   #print'El valor de pi es:PI=%.35f' %  PI
   return pi

      
n = int(sys.argv[1])
veces = int(sys.argv[2])  
print 'i              PI35DT                        lista i                           PI35DT-lista i'
for repeticion in range(1,veces+1):  
  resta = funcion(n) - PI
  print'%d %1.35f | %1.35f | %1.35f' % (repeticion, PI, funcion(n), resta)
  n = n*2
  