def mechanical_energy(mass, height, velocity):
    g = 9.81  
    potential_energy = mass * g * height
    kinetic_energy = 0.5 * mass * velocity ** 2
    total_energy = potential_energy + kinetic_energy
    return total_energy
mass = 14
height = 7 
velocity = 11 
energy = mechanical_energy(mass, height, velocity)
print(f"Полная механическая энергия: {energy}")
