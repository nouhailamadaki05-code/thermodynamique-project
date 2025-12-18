import numpy as np
Pc=1.1353*10**7
Tc=405.4
ω=0.256
T=313.15
P=700000
R=8.314
Tr=T/Tc
k=0.37464 + 1.54226*ω - 0.26992*ω**2
α=(1+k*(1-Tr**0.5)**2)
ac=0.45724*((R**2)*(Tc**2)/Pc)
b = 0.07780*(R*Tc/Pc)
at=(ac*α)
A=P
B=(b*P)-(P*b**2)-R*T
C=-R*T*2*b+(at )-(3*b**2*P)
D=R*T*b**2-(at*b)+(P*b**3)
coeffs=[A,B,C,D]
Racines=np.roots(coeffs)
print(Racines)