def get_aero_forces(weight, rho, V, S, CD0, K):
    # Find the Lift Coefficient (CL) needed for steady level flight (Lift = Weight)
    CL = (2 * weight * 9.81) / (rho * V**2 * S)
    
    # Calculate total drag using the parabolic drag polar equation
    CD = CD0 + K * (CL**2)
    
    # Total drag force (in Newtons) acting on the airframe
    drag = 0.5 * rho * V**2 * S * CD
    
    return CL, CD, drag