import pandas as pd
from faker import Faker
import random
import numpy as np

fake = Faker()

# Function to generate random data for building features
def generate_building_data(num_samples):
    np.random.seed(42)  # Set seed for reproducibility
    covariance_matrix = np.array([
        [1.0, 0.5, 0.3, 0.2, 0.2, 0.1, 0.5, 0.3, 0.2],
        [0.5, 1.0, 0.2, 0.1, 0.3, 0.2, 0.4, 0.1, 0.1],
        [0.3, 0.2, 1.0, 0.4, 0.1, 0.2, 0.3, 0.5, 0.2],
        [0.2, 0.1, 0.4, 1.0, 0.3, 0.1, 0.2, 0.4, 0.3],
        [0.2, 0.3, 0.1, 0.3, 1.0, 0.4, 0.1, 0.2, 0.1],
        [0.1, 0.2, 0.2, 0.1, 0.4, 1.0, 0.2, 0.1, 0.3],
        [0.5, 0.4, 0.3, 0.2, 0.1, 0.2, 1.0, 0.4, 0.2],
        [0.3, 0.1, 0.5, 0.4, 0.2, 0.1, 0.4, 1.0, 0.3],
        [0.2, 0.1, 0.2, 0.3, 0.1, 0.3, 0.2, 0.3, 1.0]
    ])
    
    building_data = np.random.multivariate_normal(mean=[0] * 9, cov=covariance_matrix, size=num_samples)
    
    building_data = pd.DataFrame(building_data, columns=[
        'Building_Material', 'Insulation', 'Age', 'HVAC_System',
        'Window_Type', 'Roof_Type', 'Floor_Area', 'Energy_Efficiency_Rating', 'Occupancy_Type'
    ])

    # Transforming features to be within reasonable ranges
    building_data['Age'] = np.abs(building_data['Age']) + 1
    building_data['Floor_Area'] = np.abs(building_data['Floor_Area']) + 500

    return building_data

# Function to generate random data for climate features
def generate_climate_data(num_samples):
    np.random.seed(42)  # Set seed for reproducibility
    covariance_matrix = np.array([
        [1.0, 0.5, 0.3, 0.2, 0.2, 0.1, 0.5, 0.3],
        [0.5, 1.0, 0.2, 0.1, 0.3, 0.2, 0.4, 0.1],
        [0.3, 0.2, 1.0, 0.4, 0.1, 0.2, 0.3, 0.5],
        [0.2, 0.1, 0.4, 1.0, 0.3, 0.1, 0.2, 0.4],
        [0.2, 0.3, 0.1, 0.3, 1.0, 0.4, 0.1, 0.2],
        [0.1, 0.2, 0.2, 0.1, 0.4, 1.0, 0.2, 0.1],
        [0.5, 0.4, 0.3, 0.2, 0.1, 0.2, 1.0, 0.4],
        [0.3, 0.1, 0.5, 0.4, 0.2, 0.1, 0.4, 1.0]
    ])
    
    climate_data = np.random.multivariate_normal(mean=[0] * 8, cov=covariance_matrix, size=num_samples)
    
    climate_data = pd.DataFrame(climate_data, columns=[
        'Outdoor_Temperature', 'Humidity', 'Air_Quality_Index',
        'Precipitation', 'Wind_Speed', 'Sunlight_Exposure', 'Geographical_Location', 'Elevation'
    ])

    # Transforming features to be within reasonable ranges
    climate_data['Outdoor_Temperature'] = np.clip(climate_data['Outdoor_Temperature'], -10, 40)
    climate_data['Elevation'] = np.abs(climate_data['Elevation'])

    return climate_data

# Function to generate random data for the target label
def generate_target_label(num_samples):
    np.random.seed(42)  # Set seed for reproducibility
    return np.random.choice(['Positive', 'Negative'], size=num_samples)

# Generate synthetic data
num_samples = 50000
building_data = generate_building_data(num_samples)
climate_data = generate_climate_data(num_samples)
target_labels = generate_target_label(num_samples)

# Save the generated data to a CSV file
building_data.to_csv('building_data_corr.csv', index=False)
climate_data.to_csv('climate_data_corr.csv', index=False)
pd.Series(target_labels, name='Climate_Impact').to_csv('target_labels_corr.csv', index=False)
