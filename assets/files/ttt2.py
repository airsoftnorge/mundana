import math


def calculate_time_with_air_resistance(energy_j: float, weight_g: float, distance_m: float):
    # Constants
    weight_kg = weight_g / 1000
    dragcoefficient = 0.47
    airdensity_kgm3 = 1.225
    diameter_mm = 5.95

    radius_m = diameter_mm / 1000 / 2
    crossection_m2 = math.pi * (radius_m ** 2)

    # Initial conditions
    velocity = math.sqrt(2 * energy_j / weight_kg)
    time = 0
    position = 0

    while position < distance_m:
        drag_force = 0.5 * airdensity_kgm3 * crossection_m2 * dragcoefficient * velocity ** 2
        acceleration = -drag_force / weight_kg
        velocity += acceleration * time_step
        position += velocity * time_step
        time += time_step

    if 5 > velocity:  # Remove irrelevant data as the bb is in the ground before this..
        time = 999
        return time
    return time


mindist = 0
maxdist = 120
time_step = 0.01  # Adjust the time step for numerical integration

if __name__ == "__main__":
    energy = float(input("Energy at muzzle in joule "))
    weight = float(input("Projectile weight in grams "))
    time_values = []

    for value in range(mindist, maxdist):
        time = calculate_time_with_air_resistance(energy, weight, value)
        if time < 500:
            time_values.append({"x": value, "y": time})

    print(time_values)
