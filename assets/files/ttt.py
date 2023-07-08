import math


def residual_simple(energy_j: float, weight_g: float, distance_m: float):
    if energy_j * weight_g * distance_m == 0:
        raise ValueError("Cannot have 0 as input value.")

    # Constants
    weight_kg = weight_g / 1000
    dragcoefficient = 0.47
    airdensity_kgm3 = 1.225
    diameter_mm = 5.95

    radius_m = diameter_mm / 1000 / 2
    crossection_m2 = math.pi * (radius_m ** 2)
    speed_ms = math.sqrt(energy_j / (0.5 * weight_kg))
    drag_ish = airdensity_kgm3 * crossection_m2 * dragcoefficient
    speed_at_distance = speed_ms * math.exp(-(drag_ish / (weight_kg * 2) * distance_m))
    energy_at_distance = 0.5 * weight_kg * speed_at_distance ** 2
    time = distance_m / (speed_ms + speed_at_distance)
    if speed_at_distance <= 5:
        time = 999
    return speed_at_distance, energy_at_distance, time


mindist = 1
maxdist = 150

if __name__ == "__main__":
    energy = float(input("Energy at muzzle in joule "))
    weight = float(input("Projectile weight in grams "))
    time_values = []

    for value in range(mindist, maxdist):
        speed_at_distance, energy_at_distance, time = residual_simple(energy, weight, value)
        if time == 999:
            break  # Exit the loop if time is 999
        time_tuple = (value, time)  # Create a tuple with value and time
        data_point = {"x": value, "y": time}
        time_values.append(data_point)

    print(time_values)
