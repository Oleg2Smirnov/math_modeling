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
    E = np.linspace(0, 2*np.pi, 100000)                     # эксцентрическая аномалия тела
    t = (E-e*np.sin(E))*T1/(2*np.pi)                        # время с перицентра 
    phi_1 = 2*np.arctan(np.tan(E/2)*((1+e)/(1-e))**0.5)     # истинная аномалия тела 
    phi_2 = 2*np.pi*(t/T2)                                  # истинная аномалия Земли
    r1 = A1*(1-e*np.cos(E))                                 # расстояние от Солнца до тела
    Vt1 = (G*M/p1)**0.5*(1+e*np.cos(phi_1))                 # трансверсальная тела
    Vr1 = (G*M/p1)**0.5*e*np.sin(phi_1)                     # лучевая тела
    V1 = (G*M*(2/r1-1/A1))**0.5                             # скорость тела
    V2 = (G*M/A2)**0.5                                      # скорость Земли
    theta = alpha + phi_1 - phi_2                           # разница экл долгот 
    L = (r1**2 + A2**2 - 2*r1*A2*np.cos(theta))**0.5        # расстояние между телом и Землёй
    psi = np.arcsin(np.sin(theta)*r1/L)                     # фазовый угол
    eps = np.arccos(Vr1/V1)                                 # угол между лучевой и полной тела
    gamma = np.arcsin(np.sin(theta)*A2/L)                   # элонгационный угол

    u = 2*np.pi/T2 * r1
    print('u')
    print(u)
    V = (V1**2 + u**2 - 2*u*V1*np.cos(np.pi/2-eps))**0.5
    print('V')
    print(V)
    betta = np.arcsin(np.sin(np.pi/2-eps)*u/V)
    print('betta')
    print(betta)
    g = np.pi-psi+eps-betta
    print('g')
    print(g)
    Ur = -V*np.cos(g) / 1000
    w = -V*np.sin(g)/L *180*86400/np.pi + 360*86400/T2

    plt.plot(Ur, w, label='grafic')
    plt.xlabel('Ur, км/с')
    plt.ylabel('w, градус/день')
    plt.legend()
    plt.savefig('ellips2.png')
	
ellips_plotter(A1, T1, M, e, alpha, A2, T2)
