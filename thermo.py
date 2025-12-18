import numpy as np
T=313.15
P=7e5
Tc=405.4
Pc=1.1353e7 
R=8.314
w=0.256
Tr=T/Tc
k=0.37464+1.54226*w-0.26992*w**2
x=(1+k*(1-Tr**0.5))**2
ac=0.45724*(((R**2)*(Tc**2))/Pc)
b=0.07780*(R*Tc)/Pc
at=ac*x
A=P
B=-(R*T + P*b)
C=at-3*P*b**2-2*R*T*b
D=-(at*b-P*b**3-R*T*b**2)
Vm=np.roots([A,B,C,D])
Vm_reel=np.real(Vm[np.isreal(Vm)])
Vm_physique=Vm_reel[Vm_reel>b]
print("Volumes molaires possibles:",Vm_physique)