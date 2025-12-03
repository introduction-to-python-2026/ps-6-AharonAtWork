import os
import urllib.request # Required for downloading files

def create_codon_dict(file_path):
    # 1. Ensure the data directory exists (Replaces !mkdir -p)
    # Assumes file_path is something like 'data/codons.txt'
    dir_name = os.path.dirname(file_path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True) 
    
    # 2. Download the file (Replaces !wget)
    url = "https://raw.githubusercontent.com/yotam-biu/ps6/main/data/codons.txt"
    try:
        urllib.request.urlretrieve(url, file_path) 
    except Exception as e:
        # Handle potential download errors gracefully
        print(f"Error downloading file: {e}")
        return {} # Return an empty dictionary or raise an error

    # 3. Use 'with open' for robust file reading (Good practice)
    codon_to_amino_acid_dict = {}
    try:
        with open(file_path, 'r') as file:
            rows = file.readlines()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path} after download.")
        return {}
        
    for row in rows:
        parts = row.strip().split('\t')
        # Ensure the line has enough parts before accessing index 2
        if len(parts) >= 3: 
            codon = parts[0]
            amino_acid = parts[2]
            codon_to_amino_acid_dict[codon] = amino_acid
            
    return codon_to_amino_acid_dict
