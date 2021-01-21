# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 17:38:26 2021

@author: Ryan
"""

#For Triton UAS
#determination of max height of Spar at desired locations
#source equations found at:
#airfoiltools.com/airfoil/naca4digit
#symmetrical airfoils only
#see other file for nonsymmetrical airfoils

T=(24)/100 #number provided is the last two digits of the NACA 00## airfoil

#Yt calulcation
c=1 #chord length
ao=.2969
a1=-.126
a2=-.3516
a3=.2843
a4=-.1015 #or -.1036 (close tail edge) #-.1015 (normal tail edge)
x=.2 #at what length of the span? (0-1 range of values)
yt=T*5*c*(ao*(x/c)**.5+a1*x/c+a2*(x/c)**2+a3*(x/c)**3+a4*(x/c)**4)
print("At position x=",x,"The max spar height is=",(2*yt))
