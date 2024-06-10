import json

# Load the JSON data
with open('data.json', 'r') as file:
    data = json.load(file)

# Define emission factors (example values, replace with actual values)
emission_factors = {
    "Diesel": 2.68,  # kg CO2 per liter
    "Electricity": 0.5  # kg CO2 per kWh (example value)
}

# Function to calculate CO2 emissions for a vehicle
def calculate_emissions(vehicle):
    fuel_type = vehicle["fuel_type"]
    distance_km = vehicle["distance_km"]
    emissions = 0
    
    if fuel_type == "Diesel":
        fuel_consumption_liters = vehicle["fuel_consumption_liters"]
        emissions = fuel_consumption_liters * emission_factors[fuel_type]
    elif fuel_type == "Electricity":
        energy_consumption_kWh = vehicle["energy_consumption_kWh"]
        emissions = energy_consumption_kWh * emission_factors[fuel_type]
    
    return emissions

# Create a file to save the output
output_file = 'emissions_output.txt'

with open(output_file, 'w') as f:
    # Redirect stdout to the file
    import sys
    sys.stdout = f
    
    # Calculate CO2 emissions for each vehicle
    total_emissions = 0
    for mode, vehicles in data.items():
        print(f"\n{mode} vehicles:")
        mode_emissions = 0
        for vehicle in vehicles:
            emissions = calculate_emissions(vehicle)
            mode_emissions += emissions
            print(f"{vehicle['vehicle_id']}: {emissions:.2f} kg CO2")
        print(f"Total CO2 emissions for {mode}: {mode_emissions:.2f} kg CO2")
        total_emissions += mode_emissions

    print(f"\nTotal CO2 emissions for all vehicles: {total_emissions:.2f} kg CO2")

# Reset stdout to the default
sys.stdout = sys.__stdout__

print(f"Output saved to '{output_file}'.")
