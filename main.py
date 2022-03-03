import BronstedClass as bc
import numpy as np
from scipy.optimize import fsolve
#######################################################
# TiGer - Simulator of Bronsted Acid-Base Titration   #
#######################################################

def Tisol(variaveis):
    (pH)=variaveis
    sistemaAD = bc.BronstedDados(3)
    sistemaNT = bc.BronstedDados(1)
    concAD = sistemaAD.conc
    concNT = sistemaNT.conc
    concAD=0.1
    concNT=0.1
    V0 = 10
    #meio = bc.Meio(pH)
    a, b, cargaAD = sistemaAD.alfas(pH)
    a, b, cargaNT = sistemaNT.alfas(pH)
    WAT = 10**(-float(pH))-10**(float(pH-14))
    dif = WAT+(cargaAD-sistemaAD.carga) * concAD + (cargaNT-sistemaNT.carga) * concNT
    print(pH,cargaNT,sistemaAD.carga, sistemaNT.carga,concAD)
    #
    #
    return dif

s0=np.array([-1])
s=fsolve(Tisol,s0)

print (s)


