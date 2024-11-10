import numpy as np
import pandas as pd

# Constants
m_o = 9.10938356e-31  # Mass of an electron in kg
k = 1.380649e-23  # Boltzmann constant in J/K
h = 6.62607015e-34  # Planck's constant in J·s
T = 300  # Temperature in Kelvin
e = 1.602176634e-19  # Elementary charge in C

# List to store each material's data
materials_data = []

while True:
    # Get user inputs for material name and type
    M = str(input("Enter the material name (or type 'done' to finish): "))
    if M.lower() == 'done':  # Exit loop if the user types 'done'
        break
    
    m_type = str(input("Enter the material type (ETL/HTL/PAL): "))

    # Get the values of x and y from the user
    x = float(input("Enter the value for m_n (mass multiplier for m_o): "))
    y = float(input("Enter the value for m_p (mass multiplier for m_o): "))

    # Get the value of tau from the user for this material
    tau = float(input("Enter the value for relaxation time τ (in seconds): "))

    # Calculate m_n and m_p based on user input
    m_n = x * m_o
    m_p = y * m_o

    # Calculation of N_C and N_V in m^-3
    N_C_m3 = 2 * ((2 * np.pi * m_n * k * T) / h**2)**(3/2)
    N_V_m3 = 2 * ((2 * np.pi * m_p * k * T) / h**2)**(3/2)

    # Convert N_C and N_V to cm^-3 and round to three decimal places in scientific notation
    N_C_cm3 = f"{N_C_m3 / 1e6:.3e}"
    N_V_cm3 = f"{N_V_m3 / 1e6:.3e}"

    # Calculate hole mobility (μ_p) and electron mobility (μ_n)
    mu_p = f"{(e / m_p) * tau:.3e}"
    mu_n = f"{(e / m_n) * tau:.3e}"

    # Append the data to the list in scientific notation
    materials_data.append({
        "Material": M,
        "Type": m_type,
        "N_C (cm^-3)": N_C_cm3,
        "N_V (cm^-3)": N_V_cm3,
        "μ_p (cm^2/V.s)": mu_p,
        "μ_n (cm^2/V.s)": mu_n
    })

# Create a DataFrame from the collected data
df = pd.DataFrame(materials_data)

# Display the DataFrame as a table
print("\nCollected Material Data:")
print(df)
