# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 08:15:12 2021

@author: Ryan
"""
#For Triton UAS
#determination of max height of Spar at desired locations
#source equations found at:
#airfoiltools.com/airfoil/naca4digit
#nonsymmetrical airfoils only
#see other file for symmetrical airfoils
#symmetrical airfoils will contain a 00 at the beginning
import math

NACA=list(str(2424)) #Full NACA Airfoil #will get buggy if airfoil has 00s
M=int(NACA[0])/100 #max camber
P=int(NACA[1])/10 #position of max camber
T=int(NACA[2]+NACA[3])/100 #thickness

#Yt calulcation
c=1 #chord length
ao=.2969
a1=-.126
a2=-.3516
a3=.2843
a4=-.1015 #or -.1036 (close tail edge) #-.1015 (normal tail edge)
x=.2 #at what length of the span? (0-1 range of values)
yt=T*5*c*(ao*(x/c)**.5+a1*x/c+a2*(x/c)**2+a3*(x/c)**3+a4*(x/c)**4)

#Yc calculation
#Gradient Calculation
#iteration between values of desired x and position of max camber
if (x<P*c):
    yc=((M*x)/P**2)*(2*P-(x/c)) #camber
    dycdx=(2*M/P**2)*(P-(x/c)) #gradient
elif (x>=P*c):
    yc=(M*(c-x))/(1-P)**2*(1+(x/c)-2*P) #camber
    dycdx=(2*M/(1-P)**2)*(P-(x/c)) #gradient

#theta and upper/lower surface calcs
theta=math.atan(dycdx)
xu=x-yt*math.sin(theta) #upper bound x
xl=x+yt*math.sin(theta) #lower bound x
yu=yc+yt*math.cos(theta) #upper bound y
yl=yc-yt*math.cos(theta) #lower bound y
print("At position x=",x,"The max spar height is=",(yu-yl))

