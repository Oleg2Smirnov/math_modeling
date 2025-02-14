import matplotlib.pyplot as plt
import numpy as np

M = 2*10**30                            # масса Солнца
G = 6.67*10**(-11)                      # грав конст
T1 = 1*365.26*86400                     # период обращения тела
A1 = (G*M*T1**2/4/np.pi**2)**(1/3)      # большая полуось тела
e = 0.8                                  # эксцентриситет тела
alpha = 180*np.pi/180                     # угол между начальными положениями тела и Земли (тело в перицентре)
A2 = 1.496*10**11                       # большая полуось Земли
T2 = 365.26*86400                       # период обращения Земли

fig, ax = plt.subplots()
#ax.set_xlim(-10, 10)
#ax.set_ylim(-0.2, 0.6)

def ellips_plotter(A1, T1, M, e, alpha, A2, T2):
    p1 = A1*(1-e**2)                                        # фокальный параметр тела
    E = np.linspace(0, 2*np.pi, 10000)                     # эксцентрическая аномалия тела
    t = (E-e*np.sin(E))*T1/(2*np.pi)                        # время с перицентра 
    phi_1 = 2*np.arctan(np.tan(E/2)*((1+e)/(1-e))**0.5)     # истинная аномалия тела 
    phi_2 = 2*np.pi*(t/T2)                                  # истинная аномалия Земли
    r1 = A1*(1-e*np.cos(E))                                 # расстояние от Солнца до тела
    Vt1 = (G*M/p1)**0.5*(1+e*np.cos(phi_1))                 # трансверсальная тела
    Vr1 = (G*M/p1)**0.5*e*np.sin(phi_1)                     # лучевая тела
    #print(Vr1)
    V1 = (G*M*(2/r1-1/A1))**0.5                             # скорость тела
    #print(V1)
    V2 = (G*M/A2)**0.5                                      # скорость Земли
    theta = alpha + phi_1 - phi_2                           # разница экл долгот 
    #print(theta)
    L = (r1**2 + A2**2 - 2*r1*A2*np.cos(theta))**0.5        # расстояние между телом и Землёй
    #gamma = np.arccos((-r1**2 + L**2 + A2**2)/(2*A2*L))
    gamma = np.arcsin(np.sin(theta)*r1/L)                     # элонгационный угол
    eps = np.arccos(Vr1/V1)                                 # угол между лучевой и полной тела
    #print('eps')
    #print(eps)
    #print('gamma')
    #print(gamma)
    psi = np.arcsin(np.sin(theta)*A2/L)                   # фазовый угол
    #psi = np.arccos((r1**2 + L**2 - A2**2)/(2*r1*L))
    i = np.pi + psi - eps                                 # угол между полной и трансверсальной для Земли
    #print('psi')
    #print(psi)
    print('i')
    print(i)
    #print(r1)
    Ut = V1*np.sin(i) + V2*np.cos(gamma)                # трансверсальная относительно Земли
    Ur = (-V1*np.cos(i) - V2*np.sin(gamma))/1000             # лучевая относительно Земли
    print('Ut')
    print(Ut)
    print('Ur')
    print(Ur)
    #print(L)
    w = Ut/L * 180/np.pi * 86400                           # угловая относительно Земли
    #print(w)

    plt.plot(Ur, w)#, label='')
    plt.xlabel('Ur, км/с')
    plt.ylabel('w, градус/день')
    #plt.legend()
    plt.savefig('ellips.png')
	
ellips_plotter(A1, T1, M, e, alpha, A2, T2)
