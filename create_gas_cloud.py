import sys
import numpy as np
import h5py
import random

############## initial conditions and parameters ##############
ae = 1.49e11
G = 6.67 * 10**(-11)
m_sun = 1.998 * 10**30
box_size = 20 * ae

x_centre = box_size / 2
y_centre = box_size / 2
z_centre = box_size / 2

############## PartType0 (Dark Matter) ##############
num_part = 10000
gamma = 5.0 / 3.0

m_H = 2*1.6735575e-21  # Масса молекулы водорода, кг
n_H = 2*10**10  # Характерная концентрация газа, частиц/м^3
mu_H = 0.002  # Молярная масса водорода, кг/моль
R = 8.3144598  # Газовая постоянная, Дж/(моль*К)
N_a = 6.0221409 * 10**23 # Число Авогадро 
k = 1.38064852 * 10**(-23) # Больцманская постоянная

T = np.full(num_part, 100)  # Температура, К
rho = np.full(num_part, n_H * m_H)  # Плотность водорода, кг/м^3
P = R / mu_H * rho * T
# u = P / rho / (gamma - 1)
u = 3 / 2 * rho / (n_H * mu_H) * N_a * k * T
print(u)

def vel_calc(r):
    return np.sqrt(G * m_sun / r)

# Disc
# radius_interior = ae * 0.6  # внутренний радиус диска
# radius_exterior = ae * 1.2  # внешний радиус диска
# thickness = ae * 0.2  # толщина диска

eta = 1.2348

# V_disk = np.pi * (radius_exterior**2 - radius_interior**2) * thickness
# smth_lnght = np.full(num_part, (V_disk / num_part)**(1 / 3))
# print('smth_lnght, option 1: ', smth_lnght)

# pos = np.zeros([num_part, 3])
# vel = np.zeros([num_part, 3])
#masses = V_disk / num_part * rho
# print('masses: ', masses)
#smth_lnght = eta * (masses / rho)**(1 / 3) * 10
# print('smth_lnght, option 2: ', smth_lnght)

# Sphere
sphere_radius = ae * 1  # радиус сферы
V_sphere = 4/3 * np.pi * sphere_radius**3

pos = np.zeros([num_part, 3])
vel = np.zeros([num_part, 3])

masses = V_sphere / num_part * rho

smth_lnght = eta * (masses / rho)**(1 / 3) * 10


for i in range(0, num_part):
    # theta = random.uniform(0, 2*np.pi)  # для диска 
    # radius = random.uniform(radius_interior, radius_exterior)  # для диска 

    # pos[i, 0] = x_centre + radius * np.cos(theta)  # для диска 
    # pos[i, 1] = y_centre + radius * np.sin(theta)  # для диска 
    # pos[i, 2] = z_centre + random.uniform(-thickness, thickness)  # для диска 

    # vel[i, 0] = - vel_calc(radius) * np.sin(theta)  # для диска 
    # vel[i, 1] = vel_calc(radius) * np.cos(theta)  # для диска 
    # vel[i, 2] = 0  # для диска 


    gamma = random.uniform(0, 2*np.pi)  # вдоль плоскости xy
    betta = random.uniform(0, 2*np.pi)  # вдоль оси z
    radius_vector = random.uniform(0, sphere_radius)  # радиус вектор

    pos[i, 0] = x_centre + radius_vector * np.cos(betta) * np.cos(gamma)
    pos[i, 1] = y_centre + radius_vector * np.cos(betta) * np.sin(gamma)
    pos[i, 2] = z_centre + radius_vector * np.sin(betta)

    vel[i, 0] = vel_calc(radius_vector) * np.cos(betta) * np.cos(gamma) 
    vel[i, 1] = vel_calc(radius_vector) * np.cos(betta) * np.sin(gamma) 
    vel[i, 2] = vel_calc(radius_vector) * np.sin(betta) 


############## PartType1 (Dark Matter) ##############
pos_star = np.zeros([1, 3])
pos_star[0, 0], pos_star[0, 1], pos_star[0, 2] = x_centre, y_centre, z_centre
vel_star = np.zeros([1, 3])
mass_star = np.array([m_sun])

############## Data output ##############
float_type = np.float64  
int_type = np.int32

IC = h5py.File('./IC.hdf5', 'w')

header = IC.create_group("Header")
part0 = IC.create_group("PartType0")
part1 = IC.create_group("PartType1")

NumPart = np.array([num_part, 1, 0, 0, 0, 0], dtype = int_type)
header.attrs.create("BoxSize", box_size)
header.attrs.create("UnitLength_in_cm", 100)
header.attrs.create("UnitMass_in_g", 1000)
header.attrs.create("UnitVelocity_in_cm_per_s", 100)

# Gas parts
part0.create_dataset("ParticleIDs", data=np.arange(0, num_part))
part0.create_dataset("Coordinates", data=pos)
part0.create_dataset("Velocities", data=vel)
part0.create_dataset("Masses", data=masses)
part0.create_dataset("Density", data=rho)
part0.create_dataset("InternalEnergy", data=u)

# part1
part1.create_dataset("ParticleIDs", data=np.array([num_part]))
part1.create_dataset("Coordinates", data=pos_star)
part1.create_dataset("Velocities", data=vel_star)
part1.create_dataset("Masses", data=mass_star)

############## Another parameters ##############
header.attrs.create("Composition_vector_length", 0)
header.attrs.create("Flag_Cooling", 0)
header.attrs.create("Flag_DoublePrecision", 1)
header.attrs.create("Flag_Feedback", 0)
header.attrs.create("Flag_Metals", 0)
header.attrs.create("Flag_Sfr", 0)
header.attrs.create("Flag_StellarAge", 0)
header.attrs.create("Git_commit", "unknown")
header.attrs.create("Git_date", "unknown")
header.attrs.create("HubbleParam", 1.0)
header.attrs.create("MassTable", np.zeros(6, dtype = int_type))
header.attrs.create("NumFilesPerSnapshot", 1)
header.attrs.create("NumPart_ThisFile", NumPart)
header.attrs.create("NumPart_Total", NumPart)
header.attrs.create("NumPart_Total_HighWord", np.zeros(6, dtype = int_type))
header.attrs.create("Omega0", 0.0)
header.attrs.create("OmegaBaryon", 0.0)
header.attrs.create("OmegaLambda", 0.0)
header.attrs.create("Redshift", 0.0)
header.attrs.create("Time", 0.0)

IC.close()