# BuildCare_Synthetic_data

This Python script generates synthetic data related to buildings and climate, and saves them into CSV files.

## Files

- `app.py`: The main Python script that generates the synthetic data.

## Data

The script generates the following data:

- `building_data.csv`: Contains synthetic data for buildings. Each row represents a building with various attributes.
- `climate_data.csv`: Contains synthetic data for climate. Each row represents climate data associated with a building.
- `target_labels.csv`: Contains target labels for the climate impact. Each row represents the climate impact on a corresponding building.

## How to Run

1. Ensure you have Python installed on your system.
2. Install the required dependencies using the command: `pip install -r requirements.txt`
3. Run the script using the command: `python app.py`

## Dependencies

This script requires the following Python libraries:

- pandas

These dependencies are listed in the `requirements.txt` file. You can install them using pip:

```bash
pip install -r requirements.txt