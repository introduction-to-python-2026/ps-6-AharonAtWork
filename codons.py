def create_codon_dict(file_path):
    # Ensure the data directory exists and download the file
    !mkdir -p data
    !wget -q https://raw.githubusercontent.com/yotam-biu/ps6/main/data/codons.txt -O {file_path}

    file = open(file_path)
    rows = file.readlines()
    file.close()

    codon_to_amino_acid_dict = {}
    for row in rows:
        parts = row.strip().split('\t')
        codon = parts[0]
        amino_acid = parts[2]
        codon_to_amino_acid_dict[codon] = amino_acid
    return codon_to_amino_acid_dict
