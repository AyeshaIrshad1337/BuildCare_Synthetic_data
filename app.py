import pandas as pd
from faker import Faker
import random
import numpy as np

fake = Faker()

# Function to generate random data for building features
def generate_building_data():
    return {
        'Building_Material': fake.random_element(elements=('Brick', 'Concrete', 'Steel', 'Wood')),
        'Insulation': random.uniform(0.5, 1.0) if random.choice([True, False]) else np.nan,
        'Age': random.randint(1, 50),
        'HVAC_System': fake.random_element(elements=('Central Heating', 'Heat Pump', 'Radiant Heating')),
        'Window_Type': fake.random_element(elements=('Single Pane', 'Double Pane', 'Triple Pane')),
        'Roof_Type': fake.random_element(elements=('Flat', 'Pitched', 'Shingle')),
        'Floor_Area': random.uniform(500, 5000),
        'Energy_Efficiency_Rating': random.uniform(1, 5),
        'Occupancy_Type': fake.random_element(elements=('Residential', 'Commercial', 'Industrial'))
    }

# Function to generate random data for climate features
def generate_climate_data():
    return {
        'Outdoor_Temperature': random.uniform(-10, 40),
        'Humidity': random.uniform(20, 80),
        'Air_Quality_Index': random.randint(0, 100),
        'Precipitation': random.uniform(0, 10),
        'Wind_Speed': random.uniform(0, 20),
        'Sunlight_Exposure': random.uniform(0, 12),
        'Geographical_Location': fake.random_element(elements=('Urban', 'Suburban', 'Rural')),
        'Elevation': random.uniform(0, 2000)
    }

# Function to generate random data for the target label
def generate_target_label():
    return fake.random_element(elements=('Positive', 'Negative', 'Neutral'))

# Generate synthetic data
num_samples = 50000
building_data = [generate_building_data() for _ in range(num_samples)]
climate_data = [generate_climate_data() for _ in range(num_samples)]
target_labels = [generate_target_label() for _ in range(num_samples)]

# Combine data into a DataFrame
building_data = pd.DataFrame(building_data)
climate_data = pd.DataFrame(climate_data)
target_labels = pd.Series(target_labels, name='Climate_Impact')

# Save the generated data to a CSV file
building_data.to_csv('building_data.csv', index=False)
climate_data.to_csv('climate_data.csv', index=False)
target_labels.to_csv('target_labels.csv', index=False)
