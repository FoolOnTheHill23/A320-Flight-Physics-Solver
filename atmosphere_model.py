import math

def calculate_isa(altitude_m):
    # Base ISA constants for sea level
    T0 = 288.15  # Temp in K
    P0 = 101325  # Pressure in Pa
    g = 9.80665  # Gravity in m/s^2
    R = 287.05   # Gas constant for air
    a = -0.0065  # Troposphere lapse rate (K/m)

    # Check if aircraft is in the troposphere or lower stratosphere
    if altitude_m < 11000:  
        T = T0 + a * altitude_m
        P = P0 * (T / T0) ** (-g / (a * R))
    else:  
        # Simplified stratosphere model for high-altitude cruise
        T = 216.65
        P = 22632 * math.exp(-g / (R * T) * (altitude_m - 11000))
    
    # Ideal gas law to find air density (rho)
    rho = P / (R * T)
    
    return T, P, rho