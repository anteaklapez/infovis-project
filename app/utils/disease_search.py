import json
import os

diseases = {
    # Neurological
    "Alzheimer's Disease":           {"wildtype_pdb": "1IYT", "mutant_pdb": "2BEG"},
    "Parkinson's Disease":           {"wildtype_pdb": "2N0A", "mutant_pdb": "6UFR"},
    "Huntington's Disease":          {"wildtype_pdb": "6RMH", "mutant_pdb": "6X9O"},

    # Cancers
    "Breast Cancer":                 {"wildtype_pdb": "3COJ", "mutant_pdb": "1N5O"},
    "Lung Cancer":                   {"wildtype_pdb": "2GS2", "mutant_pdb": "2ITT"},
    "Leukemia":                      {"wildtype_pdb": "2G1T", "mutant_pdb": "3QRJ"},
    "Prostate Cancer":               {"wildtype_pdb": "1E3G", "mutant_pdb": "2AX8"},

    # Metabolic & Endocrine
    "Type II Diabetes":              {"wildtype_pdb": "6Y1A", "mutant_pdb": "6ZRQ"},
    "Type I Diabetes":               {"wildtype_pdb": "2HIU", "mutant_pdb": "1XW7"},
    "Phenylketonuria*":               {"wildtype_pdb": "1PAH", "mutant_pdb": "1TG2"},

    # Cardiovascular
    "Hypertrophic Cardiomyopathy":   {"wildtype_pdb": "2MQ0", "mutant_pdb": "2MQ3"},
    "Familial Hypercholesterolemia*": {"wildtype_pdb": "1AJJ", "mutant_pdb": "1D2J"},
    "Marfan Syndrome":               {"wildtype_pdb": "1UZJ", "mutant_pdb": "1APJ"},

    # Genetic / Monogenic
    "Sickle Cell Disease":           {"wildtype_pdb": "2HHB", "mutant_pdb": "2HBS"},
    "Motor Neuron Disease (ALS)":    {"wildtype_pdb": "2C9V", "mutant_pdb": "1MFM"},
}

output_path = os.path.join(os.path.dirname(__file__), "../data/diseases_config.json")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w") as f:
    json.dump(diseases, f, indent=2)