def get_fuel_burn_rate(thrust_required, TSFC):
    # Assuming steady cruise where Thrust = Drag
    # Returns the instantaneous fuel mass flow rate (kg/s)
    return thrust_required * TSFC