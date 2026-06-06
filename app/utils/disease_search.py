import json
import os

diseases = {
    "Neurological": {
        "Alzheimer's Disease": {"wildtype_pdb": "1IYT", 
                                "mutant_pdb": "2BEG", 
                                "map_fn": "Alzheimers_Disease.csv"},
        "Parkinson's Disease": {"wildtype_pdb": "2N0A", 
                                "mutant_pdb": "6UFR", 
                                "map_fn": "Parkinsons_Disease.csv"},
        "Huntington's Disease": {"wildtype_pdb": "6RMH", 
                                 "mutant_pdb": "6X9O", 
                                 "map_fn": "Huntingtons_Disease.csv"},
    },
    "Cancers": {
        "Breast Cancer": {"wildtype_pdb": "3COJ", 
                          "mutant_pdb": "1N5O", 
                          "map_fn": "Breast_Cancer.csv"},
        "Lung Cancer": {"wildtype_pdb": "2GS2", 
                        "mutant_pdb": "2ITT", 
                        "map_fn": "Lung_Cancer.csv"},
        "Leukemia": {"wildtype_pdb": "2G1T", 
                     "mutant_pdb": "3QRJ", 
                     "map_fn": "Leukemia.csv"},
        "Prostate Cancer": {"wildtype_pdb": "1E3G", 
                            "mutant_pdb": "2AX8", 
                            "map_fn": "Prostate_Cancer.csv"},
    },
    "Metabolic & Endocrine":{
        "Type II Diabetes": {"wildtype_pdb": "6Y1A", 
                             "mutant_pdb": "6ZRQ", 
                             "map_fn": "Diabetes_Type_2.csv"},
        "Type I Diabetes": {"wildtype_pdb": "2HIU", 
                            "mutant_pdb": "1XW7",
                            "map_fn": "Diabetes_Type_1.csv"},
        "Phenylketonuria": {"wildtype_pdb": "1PAH", 
                            "mutant_pdb": "1TG2", 
                            "map_fn": "Phenylketonuria.csv"},
    },
    "Cardiovascular": { 
        "Hypertrophic Cardiomyopathy": {"wildtype_pdb": "2MQ0", 
                                        "mutant_pdb": "2MQ3", 
                                        "map_fn": "Hypertrophic_Cardiomyopathy.csv"},
        "Ischemic Stroke": {"wildtype_pdb": "3U69", 
                                          "mutant_pdb": "1THP", 
                                          "map_fn": "Ischemic_Stroke.csv"},
        "Marfan Syndrome": {"wildtype_pdb": "1UZJ", 
                            "mutant_pdb": "1APJ", 
                            "map_fn": "Marfan_Syndrome.csv"},
        },

    "Genetic / Monogenic" : {
        "Sickle Cell Disorder": {"wildtype_pdb": "2HHB", 
                                "mutant_pdb": "2HBS", 
                                "map_fn": "Sickle_Cell_Disorder.csv"},
        "Motor Neuron Disease (ALS)": {"wildtype_pdb": "2C9V", 
                                       "mutant_pdb": "1MFM", 
                                       "map_fn": "Motor_Neuron_Disease.csv"},
    }
}

output_path = os.path.join(os.path.dirname(__file__), "../data/diseases_config.json")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w") as f:
    json.dump(diseases, f, indent=2)