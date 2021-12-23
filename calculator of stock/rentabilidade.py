import numpy as np
import matplotlib.pyplot as plt

def mont(montante, taxa, tempo, adc):
    if adc == 0:
        total = montante*(1+taxa)**tempo
        return total
    else:
        total = montante
        for x in range(0,tempo,1):
            total = total*(1+taxa) + adc
             
        return total

def graf(montante, taxa, tempo, adc):
    timee = np.arange(0, tempo+1,1)
    if adc == 0:
        total = montante*(1+taxa)**tempo
        return total
    else:
        pontos = np.zeros(tempo+1)
        total = montante
        pontos[0] = total
        for x in range(0,tempo,1):
            
            total = total*(1+taxa) + adc
            pontos[x+1] = total 
        return pontos, timee, adc
def plot(b, a, c): #c = adc b= tempo a= pontos
    d = a[0]+c*b
    z = a - d
    plt.plot(b,a, color ="#3B2E8C", label ="dinheiro acumulado")
    plt.plot(b, d,color ="#222340", label ="dinheiro investido")
    plt.plot(b, z,color ="r", label ="total em juros")
    plt.grid(linestyle = '--')
    plt.ylabel("dinhero")
    plt.xlabel("meses")
    plt.title("juros compostos")
    plt.legend()
    plt.savefig('grafico.png', format = 'png')
    plt.show()

