import glob
import os
import pandas as pd
import xml.etree.ElementTree as ET

def extract_from_csv(path):
    # Find all CSV files in the specified path
    csv_pattern = os.path.join(path, '*.csv') 
    files = glob.glob(csv_pattern)
    
    # Initialize an empty DataFrame with the expected columns
    extracted_data = pd.DataFrame(columns=['car_model', 'year_of_manufacture', 'price', 'fuel'])
    
    for file in files:
        # Read the CSV file and append it to the main DataFrame
        df = pd.read_csv(file)
        extracted_data = pd.concat([extracted_data, df], ignore_index=True)
    
    return extracted_data

def extract_from_json(path):
    # Find all JSON files in the specified path
    json_pattern = os.path.join(path, '*.json')
    files = glob.glob(json_pattern)
    
    # Initialize an empty DataFrame
    extracted_data = pd.DataFrame(columns=['car_model', 'year_of_manufacture', 'price', 'fuel'])
    
    for file in files:
        # Read the JSON file (lines=True for line-delimited JSON)
        df = pd.read_json(file, lines=True)
        extracted_data = pd.concat([extracted_data, df], ignore_index=True)
        
    return extracted_data

def extract_from_xml(path):
    # Find all XML files
    xml_pattern = os.path.join(path, '*.xml')
    files = glob.glob(xml_pattern)
    
    data_list = []
    
    for file in files:
        # Parse the XML file
        tree = ET.parse(file)
        root = tree.getroot()
        
        # Iterate over each row in the XML
        for row in root:
            car_model = row.find("car_model").text
            year = int(row.find("year_of_manufacture").text)
            price = float(row.find("price").text)
            fuel = row.find("fuel").text
            
            # Append dictionary to list
            data_list.append({
                "car_model": car_model,
                "year_of_manufacture": year,
                "price": price,
                "fuel": fuel
            })
            
    return pd.DataFrame(data_list)
