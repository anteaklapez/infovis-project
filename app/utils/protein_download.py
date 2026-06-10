import json
import os
import urllib.request

diseases_dir = os.path.join(os.path.dirname(__file__), '../data/diseases_config.json')
proteins_dir = os.path.join(os.path.dirname(__file__), '../data/proteins/')

with open(diseases_dir) as f:
    config = json.load(f)

for category, diseases in config.items():
    for disease, pdbs in diseases.items():
        wildtype_pdb = pdbs["wildtype_pdb"]
        mutant_pdb = pdbs["mutant_pdb"]
        url_wildtype = (f'https://files.rcsb.org/download/{wildtype_pdb}.pdb')
        url_mutant = (f'https://files.rcsb.org/download/{mutant_pdb}.pdb')

        path_wildtype = os.path.join(proteins_dir, f'{wildtype_pdb}.pdb')
        path_mutant = os.path.join(proteins_dir, f'{mutant_pdb}.pdb')

        urllib.request.urlretrieve(url_wildtype, path_wildtype)
        urllib.request.urlretrieve(url_mutant, path_mutant)


